import json
import random

import django, hashlib
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core import exceptions

from account.models import Address
from cart.models import Cart
from checkout.models import Checkout
from product.models import Product, Tag
from seller.models import Stats


# Create your views here.

@login_required
def seller_account(request):
    if request.user.is_staff:
        if request.method == 'GET':
            return render(request, template_name='add_product.html')
        elif request.method == 'POST':
            try:
                image_files = request.FILES.getlist('image')
                # print(request.POST)
                new_product = Product()
                new_product.title = request.POST['title']
                if int(request.POST['price']) < 0:
                    print('error: '+request.POST['price'])
                    raise IOError

                new_product.price = request.POST['price']
                new_product.description = request.POST['description']
                sizes = {
                    'sizes': [
                        {
                            'size': 'XS',
                            'qty': request.POST['size-xs']
                        },
                        {
                            'size': 'S',
                            'qty': request.POST['size-s']
                        },
                        {
                            'size': 'M',
                            'qty': request.POST['size-m']
                        },
                        {
                            'size': 'L',
                            'qty': request.POST['size-l']
                        },
                        {
                            'size': 'XL',
                            'qty': request.POST['size-xl']
                        },
                    ]
                }
                for s in sizes['sizes']:
                    if int(s['qty']) < 0:
                        print('error: '+s['qty'])
                        raise IOError
                sizes = json.dumps(sizes)

                new_product.available_sizes = sizes
                for image_file in image_files:
                    sha256_hash = hashlib.sha256()
                    image_title = str(image_file)
                    image_extension = str(image_file).split('.')
                    image_extension = '.' + image_extension[len(image_extension) - 1]
                    sha256_hash.update(image_title.encode('utf-8'))
                    image_title = sha256_hash.hexdigest()
                    if new_product.img1 == '':
                        new_product.img1 = 'uploaded/' + image_title + image_extension
                    elif new_product.img2 == '':
                        new_product.img2 = 'uploaded/' + image_title + image_extension

                    save_uploaded_image(image_file, image_title, image_extension)

                new_product.save()

                for cat_tag in request.POST.getlist('cat-tag'):
                    cat_tag = str(cat_tag).capitalize()
                    Tag.objects.get_or_create(name=cat_tag, type='cat')
                    new_product.category_tags.add(Tag.objects.get(name=cat_tag).id)
                for color_tag in request.POST.getlist('color-tag'):
                    color_tag = str(color_tag).capitalize()
                    Tag.objects.get_or_create(name=color_tag, type='col')
                    new_product.color_tags.add(Tag.objects.get(name=color_tag).id)

                new_product.save()

                return redirect('/account/seller/#success')
            except :
                return redirect('/account/seller/#missing_fields')

    else:
        raise exceptions.PermissionDenied()


def save_uploaded_image(image_file, title, ext):
    with open('static/images/uploaded/' + title + ext, 'wb') as destination:
        for chunk in image_file.chunks():
            destination.write(chunk)


@login_required
def rm_product(request):
    if request.user.is_staff:
        if request.method == 'GET':
            ctx = {
                'products': Product.objects.all().filter(for_sale=True)
            }
            return render(request, template_name='rm_product.html', context=ctx)
        elif request.method == 'POST':
            for pid in request.POST.getlist('remove'):
                p = Product.objects.get(pid=pid)
                p.for_sale = False
                p.save()
            ctx = {
                'products': Product.objects.all().filter(for_sale=True)
            }
            return render(request, template_name='rm_product.html', context=ctx)
    else:
        raise exceptions.PermissionDenied()


@login_required
def all_orders(request):
    if request.user.is_staff and request.method == 'GET':
        ctx = {
            'orders': Checkout.objects.all(),
        }
        return render(request, template_name='all_orders.html', context=ctx)
    else:
        raise exceptions.PermissionDenied()


@login_required
def stats(request):
    if request.user.is_staff and request.method == 'GET':

        for product in Product.objects.all():
            (stats, created) = Stats.objects.get_or_create(product_id=product.pid)
            stats.calc_stats()
            stats.calc_avg_stars()
            stats.calc_feedback()
            stats.save()

        ctx = {
            'stats': Stats.objects.all()
        }

        return render(request, template_name='stats.html', context=ctx)
    else:
        raise exceptions.PermissionDenied()
