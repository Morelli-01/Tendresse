import datetime
import json

from django.core import exceptions
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, redirect

from cart.models import Cart
from product.models import Product


# Create your views here.

def cart(request):
    ctx = {
        'cart=': '',
        'products': '',
    }
    if request.user.is_authenticated:
        if not Cart.objects.all().filter(user=request.user, checked_out=0).exists():
            return render(request, template_name='cart.html', context=ctx)
        cart = Cart.objects.all().filter(user=request.user, checked_out=0).first()
        ctx = {
            'cart': cart
        }
    else:
        if not request.user.is_authenticated:
            if not Cart.objects.all().filter(ip=request.META.get('REMOTE_ADDR'), checked_out=0).exists():
                return render(request, template_name='cart.html', context=ctx)
        cart = Cart.objects.all().filter(ip=request.META.get('REMOTE_ADDR'), checked_out=0).first()

        if not check_cart_validity(cart):
            cart.delete()
            cart = Cart()
            cart.ip = request.META.get('REMOTE_ADDR')
        cart.validity = datetime.date.today() + datetime.timedelta(days=2)
        ctx = {
            'cart': cart
        }
    qset = Product.objects.none()
    results = []

    prod_cart = json.loads(str(cart.products))
    # print(prod_cart)
    # print(prod_cart['0'])
    for p in prod_cart:
        p = prod_cart[p]
        results.append(Product.objects.all().filter(pid=p['pid']))
    for r in results:
        qset = qset.union(qset, r)

    ctx['products'] = qset
    return render(request, template_name='cart.html', context=ctx)


def atc(request):
    if request.method == 'GET':
        raise exceptions.BadRequest("Method not allowed")

    cart = Cart()
    if request.method == 'POST':
        payload = json.loads(request.body)

        if not check_size_availability(payload):
            return HttpResponse(status=406)

        if request.user.is_authenticated:
            if Cart.objects.all().filter(user=request.user, checked_out=0).exists():
                cart = Cart.objects.all().filter(user=request.user, checked_out=0).first()
            else:
                cart.user = request.user
        else:
            if Cart.objects.all().filter(ip=request.META.get('REMOTE_ADDR'), checked_out=0).exists():
                cart = Cart.objects.all().filter(ip=request.META.get('REMOTE_ADDR'), checked_out=0).first()

                if not check_cart_validity(cart):
                    cart.delete()
                    cart = Cart()
                    cart.ip = request.META.get('REMOTE_ADDR')

                cart.validity = datetime.date.today() + datetime.timedelta(days=2)

            else:
                cart.validity = datetime.date.today() + datetime.timedelta(days=2)
                cart.ip = request.META.get('REMOTE_ADDR')
    if cart.products:
        product_cart = json.loads(cart.products)
    else:
        product_cart = {}
    if cart.products:
        for p in product_cart:
            if product_cart[p]['pid'] == payload['pid'] and product_cart[p]['size'] == payload['size']:
                product_cart[p]['qty'] = str(int(product_cart[p]['qty']) + int(payload['qty']))
                payload = ''

        if not payload == '':
            product_cart[str(len(product_cart.keys()))] = payload

        cart.products = json.dumps(product_cart)
    else:
        cart.products = json.dumps({
            '0': payload
        })
    cart.save()

    return HttpResponse(status=201)


def rfc(request):
    if request.method == 'GET':
        raise exceptions.BadRequest("Method not allowed")
    # print(json.loads(request.body))
    index = json.loads(request.body)['product_index']
    if request.user.is_authenticated:
        cart = Cart.objects.all().filter(user=request.user, checked_out=0).first()
    else:
        cart = Cart.objects.all().filter(ip=request.META.get('REMOTE_ADDR'), checked_out=0).first()

    p = json.loads(cart.products)

    product_cart = {}
    flag = 0
    for i in p:
        if i == index:
            flag = -1
            continue
        product_cart[str(int(i) + flag)] = p[i]

    cart.products = json.dumps(product_cart)
    cart.save()

    return HttpResponse(status=204)


def get_n_items(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            if Cart.objects.all().filter(user=request.user, checked_out=0).exists():
                cart = Cart.objects.all().filter(user=request.user, checked_out=0).first()
            else:
                return HttpResponse('0')
        else:
            if Cart.objects.all().filter(ip=request.META.get('REMOTE_ADDR'), checked_out=0).exists():
                cart = Cart.objects.all().filter(ip=request.META.get('REMOTE_ADDR'), checked_out=0).first()
            else:
                return HttpResponse('0')
    # print(json.loads(cart.products))
    return HttpResponse(str(len(json.loads(cart.products))))


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
