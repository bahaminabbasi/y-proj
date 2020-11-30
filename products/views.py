from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from carts.models import Cart
from .models import Product
from iteminfo.models import Category, SubCategory

import persian

def products_list(request):
    qss     = Product.objects.all()
    paginator = Paginator(qss, 12)
    page      = request.GET.get('page')
    try:
        qs  = paginator.page(page)
    except EmptyPage:
        qs  = paginator.page(paginator.num_page)
    except PageNotAnInteger:
        qs  = paginator.page(1)
    context = {
        'products': qs,
    }
    return render(request, 'products/products_list.html', context)


def product_detail(request, slug):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    qs = Product.objects.filter(slug=slug)
    if qs.exists():
        product = qs.first()
        product_price = persian.convert_en_numbers(product.price)
    else:
        return HttpResponse('not found')
    context = {
        'product': product,
        'product_price': product_price,
        'cart': cart_obj,
    }
    return render(request, 'products/product_detail.html', context)

def product_filter(request, cat, level):
    if level == 0:
        category = Category.objects.filter(slug=cat).first()
        if category is not None:
            qs = Product.objects.filter(category=category.id)
            category_qs = SubCategory.objects.filter(parent=category, nesting_level=1)
            print(category_qs)
        else:
            return render(request, 'main/error.html')
        context = {
            'products': qs,
            'category_qs': category_qs,
            'page_title': category.name
        }
    else:
        sub_cat = SubCategory.objects.filter(slug=cat).first()
        if sub_cat is not None:
            qs = Product.objects.filter(sub_category=sub_cat.id)
        else:
            return render(request, 'main/error.html')
        context = {
            'products': qs,
            
            'page_title': sub_cat.name,
        }
    # else:
    #      return render(request, 'main/test.html')
    return render(request, 'products/products_list.html', context)