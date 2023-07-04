import datetime
import json

from django.core import exceptions
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, redirect

from cart.models import Cart, Product_in_Cart
from product.models import Product


# Create your views here.

def cart(request):
    ctx = {
        'cart': '',
    }
    if request.user.is_authenticated:
        if not Cart.objects.all().filter(user=request.user, checked_out=0).exists():
            return render(request, template_name='cart.html', context=ctx)
        cart = Cart.objects.get(user=request.user, checked_out=0)
        ctx['cart'] = cart

    else:
        if not Cart.objects.all().filter(ip=request.META.get('REMOTE_ADDR'), checked_out=0).exists():
            return render(request, template_name='cart.html', context=ctx)

        cart = Cart.objects.get(ip=request.META.get('REMOTE_ADDR'), checked_out=0)

        if not check_cart_validity(cart):
            cart.delete()
            cart = Cart()
            cart.ip = request.META.get('REMOTE_ADDR')
        cart.validity = datetime.date.today() + datetime.timedelta(days=2)
        ctx['cart'] = cart


    products = cart.products_in_cart.all()
    ctx['products_in_cart']=products

    return render(request, template_name='cart.html', context=ctx)


def atc(request):
    if request.method == 'GET':
        raise exceptions.BadRequest("Method not allowed")
    elif request.method == 'POST':
        cart = fetch_cart(request)
        cart.save()
        payload = json.loads(request.body)
        if not check_size_availability(payload):
            return HttpResponse(status=406)

        prod_in_cart = Product_in_Cart()
        prod_in_cart.product = Product.objects.get(pid=payload['pid'])
        prod_in_cart.qty = payload['qty']
        prod_in_cart.size = payload['size']
        prod_in_cart.save()
        to_be_added = True
        for pc in cart.products_in_cart.all():
            if pc.product == prod_in_cart.product and pc.size == prod_in_cart.size:
                pc.qty += int(prod_in_cart.qty)
                pc.save()
                to_be_added = False
        if to_be_added:

            cart.products_in_cart.add(prod_in_cart)

        cart.save()

    return HttpResponse(status=201)


def rfc(request):
    if request.method == 'GET':
        raise exceptions.BadRequest("Method not allowed")
    payload = json.loads(request.body)
    pic = payload['pic']

    if request.user.is_authenticated:
        cart = Cart.objects.all().get(user=request.user, checked_out=0)
    else:
        cart = Cart.objects.all().get(ip=request.META.get('REMOTE_ADDR'), checked_out=0)

    cart.products_in_cart.get(id=pic).delete()
    cart.save()

    return HttpResponse(status=204)


def get_n_items(request):
    if request.method == 'GET':
        try:
            cart = fetch_cart(request)
            n_items = cart.products_in_cart.all().count()
            return HttpResponse(str(n_items))
        except:
            return HttpResponse('0')


def check_cart_validity(cart: Cart):
    # print(cart.validity.date())
    if cart.validity.date() < datetime.date.today():
        return False
    if cart.checked_out == 1:
        return False

    return True


def check_size_availability(product):
    requested_qty = product['qty']
    requested_size = product['size']
    pid = product['pid']

    # print(json.loads(Product.objects.get(pid=pid).available_sizes)['sizes'])
    for p in json.loads(Product.objects.get(pid=pid).available_sizes)['sizes']:
        if p['size'] == requested_size and int(p['qty']) < int(requested_qty):
            return False

    return True


def fetch_cart(request):
    if request.user.is_authenticated:
        if Cart.objects.all().filter(user=request.user, checked_out=0).exists():
            return Cart.objects.get(user=request.user, checked_out=0)
        else:
            return Cart(user=request.user)
    else:
        if Cart.objects.all().filter(ip=request.META.get('REMOTE_ADDR'), checked_out=0).exists():
            cart = Cart.objects.get(ip=request.META.get('REMOTE_ADDR'), checked_out=0)
            if not check_cart_validity(cart):
                cart.delete()
                cart = Cart()
                cart.products = '{}'
                cart.ip = request.META.get('REMOTE_ADDR')

        else:
            cart = Cart()
            cart.ip = request.META.get('REMOTE_ADDR')
            cart.products = '{}'

        cart.validity = datetime.date.today() + datetime.timedelta(days=2)
        return cart
