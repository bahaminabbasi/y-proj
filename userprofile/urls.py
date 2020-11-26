from django.urls import path

from .views import main_profile_page

app_name = 'userprofile'

urlpatterns = [
    path('home/<int:id>', main_profile_page, name='main-profile-page'),
]