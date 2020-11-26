from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('phonecheck/', views.phone_check_message, name='phone-check-message'),
    path('confirm/', views.phone_confirm, name='confirm'),
    path('setpassword/', views.set_password_register, name='set-password-register'),
    path('changepasswordphone/', views.change_password_phone, name='change-password-phone'),
    path('changepasswordconfrim/', views.change_password_confrim, name='change-password-confrim'),
    path('setnewpass/', views.set_new_password, name='set-new-password'),

]