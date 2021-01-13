from django.urls import path

from . import views

app_name = 'carts'

urlpatterns = [
    path('', views.cart_home, name='home'),
    path('update/', views.cart_update, name='update'),
    path('maxlimit/', views.maxlimit, name='maxlimit'),
    # path('minlimit/', views.minlimit, name='minlimit'),
]