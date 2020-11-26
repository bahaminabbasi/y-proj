from django.urls import path

from .views import (
    dashboard_home,
    add_product,
    tables,
    edit_product,
    delete_product,
    delete_product_confirmed,
    add_main_slider,
    choose_main_slider,
    levelzero_selected,
    levelone_selected,
    leveltwo_selected,
    )

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard_home, name='home'),
    path('addproduct/', add_product, name='add-product'),
    path('tables/', tables, name='tables'),
    path('editproduct/<int:id>', edit_product, name='edit-product'),
    path('deleteprocut/<int:id>', delete_product, name='delete-product'),
    path('deleteprocutconfirmed/<int:id>', delete_product_confirmed, name='delete-product-confirmed'),
    path('addmainslider/', add_main_slider, name='add-main-slider'),
    path('choosemainslider/', choose_main_slider, name='choose-main-slider'),

    # AJAX 
    path('levelzero_selected/', levelzero_selected, name='levelzero-selected'),
    path('levelone_selected/', levelone_selected, name='levelone-selected'),
    path('leveltwo_selected/', leveltwo_selected, name='leveltwo-selected'),
]