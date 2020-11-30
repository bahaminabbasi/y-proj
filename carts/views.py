from django.shortcuts import render, redirect

from products.models import Product
from .models import Cart


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, 'carts/store.html', {'cart': cart_obj})


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            prodcut_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print('show message to user, product is gone!')
            return redirect('carts:home')
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if prodcut_obj in cart_obj.products.all():
            cart_obj.products.remove(product_id) # removed should be removed and plus one should be implemented
        else:
            cart_obj.products.add(prodcut_obj)
    return redirect('carts:home')

