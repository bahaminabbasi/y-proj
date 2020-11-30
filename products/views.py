from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Product
from .filters import ProductFilter
from carts.models import Cart
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
            products = Product.objects.filter(category=category.id)
            myFilter = ProductFilter(request.GET, queryset=products)
            products = myFilter.qs
            category_qs = SubCategory.objects.filter(parent=category, nesting_level=1)
            print(category_qs)
        else:
            return render(request, 'main/error.html')
        context = {
            'products': products,
            'category_qs': category_qs,
            'page_title': category.name,
            'myFilter': myFilter
        }
    else:
        sub_cat = SubCategory.objects.filter(slug=cat).first()
        if sub_cat is not None:
            products = Product.objects.filter(sub_category=sub_cat.id)
        else:
            return render(request, 'main/error.html')
        context = {
            'products': products,
            'page_title': sub_cat.name,
        }
    return render(request, 'products/products_list.html', context)