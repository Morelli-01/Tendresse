import json

import django.core.exceptions
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from account.models import *
from cart.models import Cart
from checkout.models import Checkout
from product.models import Product


# Create your views here.


@login_required
def account(request):
    return render(request, template_name='account_detail.html')


@login_required
def edit_account(request):
    if request.method == 'GET':
        return redirect('/account')
    if request.method == 'POST':
        request.user.first_name = request.POST['name']
        request.user.last_name = request.POST['surname']
        request.user.email = request.POST['email']
        request.user.username = request.POST['email']
        request.user.password = request.POST['password']
        request.user.save()
        return redirect('/account#edited')


@login_required
def add_address(request):
    if request.method == 'GET':
        print(request.headers)
        print(request.body)
        return redirect('/account')
    if request.method == 'POST':
        # print(request.body)
        for p in request.POST:
            if p == 'line2':
                continue
            if request.POST[p] == '':
                return redirect('/account#missing_fields')
        address = Address()
        address.name = request.POST['name']
        address.surname = request.POST['surname']
        address.line1 = request.POST['line1']
        address.line2 = request.POST['line2']
        address.city = request.POST['city']
        address.province = request.POST['province']
        address.zip = request.POST['zip']
        address.user = request.user
        if Address.objects.all().filter(name=address.name, surname=address.surname, line1=address.line1).exists():
            return redirect('/account#address_already_exist')
        try:
            address.save()
            if 'from-checkout' in request.POST:
                return redirect('/checkout/1')
            return redirect('/account#edited')
        except:
            print('error trying to save address')
            print(address)
            return redirect('/account')


@login_required
def addresses(request):
    ctx = {
        'addresses': Address.objects.all().filter(user_id=request.user.username)
    }
    return render(request, template_name='account_address.html', context=ctx)


@login_required
def addresses_edit(request, id):
    if (request.method == 'GET'):
        ctx = {
            'addresses': Address.objects.all().filter(user_id=request.user.username),
            'address_to_edit': Address.objects.all().filter(id=id).first()
        }
        return render(request, template_name='account_address_edit.html', context=ctx)
    if (request.method == 'POST'):
        addr_to_edit = Address.objects.all().filter(id=id).first()
        addr_to_edit.name = request.POST['name']
        addr_to_edit.surname = request.POST['surname']
        addr_to_edit.line1 = request.POST['line1']
        addr_to_edit.line2 = request.POST['line2']
        addr_to_edit.city = request.POST['city']
        addr_to_edit.province = request.POST['province']
        addr_to_edit.zip = request.POST['zip']
        addr_to_edit.user = request.user
        addr_to_edit.save()

        return redirect(to='/account/addresses')


@login_required
def addresses_delete(request, id):
    Address.objects.all().filter(id=id).delete()
    return redirect(to='/account/addresses')


@login_required
def orders(request):
    if not Checkout.objects.all().filter(user=request.user, confirmed=1).exists():
        ctx = {
            'orders': ''
        }
        return render(request, template_name='account_orders.html', context=ctx)
    ctx = {
        'orders': Checkout.objects.all().filter(user=request.user, confirmed=1)
    }

    carts = Cart.objects.all().filter(user=request.user, checked_out=1)
    ctx['carts'] = carts

    qset = Product.objects.none()
    pids = []
    for cart in carts:
        products = json.loads(cart.products)
        for p in products:
            if not pids.__contains__(products[p]['pid']):
                pids.append(products[p]['pid'])

    # print(pids)
    for pid in pids:
        prods = Product.objects.all().filter(pid=pid)
        qset = qset.union(qset, prods)

    ctx['products'] = qset
    # print(ctx)

    ctx['addresses'] = Address.objects.all().filter(user=request.user)
    ctx['feedbacks'] = Feedback.objects.all().filter(user=request.user)

    if request.method == 'POST':
        print(request.body)
        feed = Feedback()
        feed.user = request.user
        feed.product = Product.objects.get(pid=request.POST['pid-input'])
        feed.comment = request.POST['comment']
        feed.stars = int(request.POST['star-count'])
        try:
            feed.save()
        except:
            redirect(to='/account/order#feed_err')
    return render(request, template_name='account_orders.html', context=ctx) \

@login_required
def feedbacks(request):
    ctx = {
        'feedbacks':Feedback.objects.all().filter(user=request.user),
    }
    if request.method == 'POST':
        feedback_id = request.POST['feedback-id']
        Feedback.objects.get(id=feedback_id).delete()

    return render(request, template_name='feedbacks.html', context=ctx)
