import django_filters
from django.db import models
from django import forms

from .models import Product
from iteminfo.models import Category


class ProductFilter(django_filters.FilterSet): 
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    brand_name = django_filters.ChoiceFilter(field_name='brand_name')
    class Meta:
        model = Product
        fields = ['brand_name', ]