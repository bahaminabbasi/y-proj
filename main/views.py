from django.shortcuts import render, HttpResponse

from .models import MainPictures
from products.models import Product
from carts.models import Cart


def home(request):
    return render(request, 'main/home.html')

