from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from accounts.models import User

@login_required
def main_profile_page(request, id):
    user = User.objects.filter(pk=id).first()
    user_profile = UserProfile.objects.filter(user_name=user).first()   
    context = {
        'user': user,
        'user_profile': user_profile,
    }
    return render(request, 'userprofile/main_profile_page.html', context)


@login_required
def edit_profile(request):
    return render(request, 'userprofile/edit_profile.html')