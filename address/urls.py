from django.urls import path
from . import views

app_name = 'address'

urlpatterns = [
    path('add/', views.add_address, name='add-address'),
]