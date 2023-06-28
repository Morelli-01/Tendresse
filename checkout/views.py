import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core import exceptions

from account.models import Address
from cart.models import Cart
from checkout.models import Checkout
from product.models import Product


# Create your views here.
@login_required
def checkout_stage_1(request):
    if request.method == 'GET':
        ctx = {
            'addresses': Address.objects.all().filter(user=request.user)
        }
        return render(request, template_name='checkout1.html', context=ctx)
    elif request.method == 'POST':
        payload = json.loads(request.body)
        print(payload)
        if Checkout.objects.all().filter(user=request.user, confirmed=0).exists():
            Checkout.objects.all().filter(user=request.user, confirmed=0).first().delete()
        checkout = Checkout()
        checkout.user = request.user
        checkout.confirmed = False
        checkout.cart = Cart.objects.all().filter(user=request.user, checked_out=0).first()
        checkout.ship_method = payload['ship_method']
        checkout.addr = Address.objects.all().filter(id=payload['addr_id']).first()

        prezzo_finale = 0
        cart = json.loads(checkout.cart.products)
        for i in cart:
            prezzo_finale += int(cart[i]['qty']) * float(Product.objects.all().filter(pid=cart[i]['pid']).first().price)
        if checkout.ship_method == 'standard':
            prezzo_finale += 10
        checkout.total_price = prezzo_finale
        checkout.save()
        return render(request, template_name='checkout1.html')


@login_required
def checkout_stage_2(request):
    if not Checkout.objects.all().filter(user=request.user, confirmed=0).exists():
        raise exceptions.RequestAborted('Before you have to complete checkout\'s step-1')
    if request.method == 'GET':
        ctx = {
            'checkout': Checkout.objects.all().filter(user=request.user, confirmed=0).first()
        }
        return render(request, template_name='checkout2.html', context=ctx)
    elif request.method == 'POST':
        checkout = Checkout.objects.all().filter(user=request.user, confirmed=0).first()
        payload = json.loads(request.body)
        checkout.payment_method = payload['payment_method']
        # check coerenza pagamento e ship
        if checkout.payment_method == 'collect' and checkout.ship_method != 'collect':
            return HttpResponse(status=409)
        # check disponibilità taglie e nel caso abbasso di esse
        if not check_size_availability(json.loads(checkout.cart.products)):
            return HttpResponse(status=406)
        checkout.confirmed = True
        checkout.save()

        cart = Cart.objects.all().get(id=checkout.cart.id)
        cart.checked_out = True
        cart.save()

        decrease_availability(cart)
        return HttpResponse(status=201)


def check_size_availability(products):
    for i in products:
        requested_qty = products[i]['qty']
        requested_size = products[i]['size']
        pid = products[i]['pid']

        # print(json.loads(Product.objects.get(pid=pid).available_sizes)['sizes'])
        for p in json.loads(Product.objects.get(pid=pid).available_sizes)['sizes']:
            if p['size'] == requested_size and int(p['qty']) < int(requested_qty):
                return False
    return True


def decrease_availability(cart: Cart):
    products = json.loads(cart.products)
    for i in products:
        qty_to_remove = products[i]['qty']
        size_to_remove = products[i]['size']

        pid = products[i]['pid']
        p = Product.objects.get(pid=pid)
        availability = json.loads(p.available_sizes)
        if size_to_remove == 'XS':
            availability['sizes'][0]['qty'] = str(int(availability['sizes'][0]['qty']) - int(qty_to_remove))
        elif size_to_remove == 'S':
            availability['sizes'][1]['qty'] = str(int(availability['sizes'][1]['qty']) - int(qty_to_remove))
        elif size_to_remove == 'M':
            availability['sizes'][2]['qty'] = str(int(availability['sizes'][2]['qty']) - int(qty_to_remove))
        elif size_to_remove == 'L':
            availability['sizes'][3]['qty'] = str(int(availability['sizes'][3]['qty']) - int(qty_to_remove))
        elif size_to_remove == 'XL':
            availability['sizes'][4]['qty'] = str(int(availability['sizes'][4]['qty']) - int(qty_to_remove))

        p.available_sizes = json.dumps(availability)
        p.save()