from django.urls import path

from .views import main_profile_page, edit_profile, UpUpdate

app_name = 'userprofile'

urlpatterns = [
    path('home/<int:id>', main_profile_page, name='main-profile-page'),
    path('editprofile/', edit_profile, name='edit-profile'),
    path('upup/', UpUpdate, name='up-up'),
]