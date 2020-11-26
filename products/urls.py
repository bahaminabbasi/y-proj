from django.urls import path

from .views import products_list, product_detail, product_filter

app_name = 'products'

urlpatterns = [
    path('list/', products_list, name='list'),
    path('detail/<slug:slug>', product_detail, name='detail'),
    path('list/category/<str:cat>/<int:level>', product_filter, name='product-filter'),
]