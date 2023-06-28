import json

from django.db.models import QuerySet
from django.shortcuts import render

from account.models import Feedback
from .models import *


# Create your views here.
def products(request):
    if request.method == 'GET':
        # print(list(request.GET.keys()))
        if len(list(request.GET.keys())) > 0:
            results_cat = Product.objects.all().filter(for_sale=True)
            results_col = Product.objects.all().filter(for_sale=True)
            requested_tags = list(request.GET.keys())
            for req_tag in requested_tags:
                req_tag = Tag.objects.all().get(name=req_tag)
                if req_tag.type == 'cat':
                    if len(results_cat) == len(Product.objects.all().filter(for_sale=True)):
                        results_cat = Product.objects.none()
                    results_cat = results_cat.union(results_cat,
                                                    Product.objects.all().filter(category_tags=req_tag, for_sale=True))
                else:
                    if len(results_col) == len(Product.objects.all().filter(for_sale=True)):
                        results_col = Product.objects.none()
                    results_col = results_col.union(results_col,
                                                    Product.objects.all().filter(color_tags=req_tag, for_sale=True))

            results = results_cat.intersection(results_cat, results_col)
            ctx = {
                'products': results,
                'cat_tags': Tag.objects.all().filter(type='cat'),
                'col_tags': Tag.objects.all().filter(type='col'),
            }
            return render(request, template_name='products.html', context=ctx)

        ctx = {
            'products': Product.objects.all().filter(for_sale=True),
            'cat_tags': Tag.objects.all().filter(type='cat'),
            'col_tags': Tag.objects.all().filter(type='col'),
        }
        #
        # for t in Tag.objects.all().filter(type='cat'):
        #     # print(t.name)

        return render(request, template_name='products.html', context=ctx)
    elif request.method == 'POST':
        ctx = {
            'products': Product.objects.all().filter(title__contains=request.POST['search-keys'], for_sale=True),
            'n_results': len(Product.objects.all().filter(title__contains=request.POST['search-keys'], for_sale=True)),
            'cat_tags': Tag.objects.all().filter(type='cat'),
            'col_tags': Tag.objects.all().filter(type='col'),
        }
        return render(request, template_name='products.html', context=ctx)


def product(request, pid):
    product = Product.objects.get(pid=pid, for_sale=True)
    av_sizes = json.loads(product.available_sizes)['sizes']
    sizes = []
    for s in av_sizes:
        sizes.append(s['qty'])
    # print(sizes)
    related_prod = Product.objects.none()
    for tag in product.category_tags.all():
        related_prod = related_prod.union(related_prod, Product.objects.all().filter(category_tags=tag, for_sale=True))

    for tag in product.color_tags.all():
        related_prod = related_prod.union(related_prod, Product.objects.all().filter(color_tags=tag, for_sale=True))

    ctx = {
        'product': product,
        'sizes': sizes,
        'feedbacks': Feedback.objects.all().filter(product=product),
        'products': related_prod
    }

    return render(request, template_name='product.html', context=ctx)


def products_ordered(request, type):
    if request.method == 'GET':
        results = Product.objects.none()
        if len(list(request.GET.keys())) > 0:
            requested_tags = list(request.GET.keys())
            for req_tag in requested_tags:
                req_tag = Tag.objects.all().get(name=req_tag)
                results = results.union(results, Product.objects.all().filter(color_tags=req_tag, for_sale=True))
                results = results.union(results, Product.objects.all().filter(category_tags=req_tag, for_sale=True))
        else:
            results = Product.objects.all().filter(for_sale=True)

        if type == 'price-increase':
            products = results.order_by('price')
        else:
            products = results.order_by('-price')
        ctx = {
            'products': products,
            'cat_tags': Tag.objects.all().filter(type='cat'),
            'col_tags': Tag.objects.all().filter(type='col'),
        }

        return render(request, template_name='products.html', context=ctx)
    elif request.method == 'POST':

        results = Product.objects.all().filter(title__contains=request.POST['search-keys'], for_sale=True)
        if type == 'price-increase':
            products = results.order_by('price')
        else:
            products = results.order_by('-price')
        ctx = {
            'products': products,
            'n_results': len(Product.objects.all().filter(title__contains=request.POST['search-keys'], for_sale=True)),
            'cat_tags': Tag.objects.all().filter(type='cat'),
            'col_tags': Tag.objects.all().filter(type='col'),
        }
        return render(request, template_name='products.html', context=ctx)
