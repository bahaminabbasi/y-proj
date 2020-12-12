from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from accounts.models import User
from .forms import UserProfileForm

from django.views.generic.edit import UpdateView



@login_required
def main_profile_page(request, id):
    user = User.objects.filter(pk=id).first()
    user_profile = UserProfile.objects.filter(user_name=user).first()   
    context = {
        'user': user,
        'user_profile': user_profile,
        'active_tab': 'main',
    }
    return render(request, 'userprofile/main_profile_page.html', context)


@login_required
def edit_profile(request):
    user = request.user
    user_profile = UserProfile.objects.filter(user_name=user).first()
    if request.method == 'POST':
        print(request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact_number = request.POST.get('contact_number')
        melli_code = request.POST.get('melli_code')
        email = request.POST.get('email')
        user_profile.first_name = first_name
        user_profile.last_name = last_name
        user_profile.contact_number = contact_number
        user_profile.melli_code = melli_code
        user_profile.email = email
        user_profile.save()
        return redirect('userprofile:main-profile-page', id=user.id)

    else:
        # form = UserProfileForm()
        pass
    context = {
        'user': user,
        'up': user_profile,
    }
    return render(request, 'userprofile/edit_profile.html', context)

