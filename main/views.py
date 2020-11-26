from django.shortcuts import render, HttpResponse

from .models import MainPictures
from products.models import Product
from carts.models import Cart


def home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)

    # pic_obj = MainPictures.objects.get(name='nuxe')
    
    

    return render(request, 'main/home.html', {'cart': cart_obj})

def test(request):
    product = Product.objects.filter(english_title='laptop').first()

    return render(request, 'main/test.html', {'product': product})