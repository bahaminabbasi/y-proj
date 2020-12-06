from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from accounts.models import User
from .forms import UserProfileForm


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
    form = UserProfileForm()
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = UserProfile.objects.filter(user_name=user).first()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            contact_number = form.cleaned_data.get('contact_number')
            melli_code = form.cleaned_data.get('melli_code')
            email = form.cleaned_data.get('email')
            # print(user_profile, first_name, last_name, contact_number, melli_code, email)
            user_profile.first_name = first_name
            user_profile.last_name = last_name
            user_profile.contact_number = contact_number
            user_profile.melli_code = melli_code
            user_profile.email = email
            user_profile.save()
            return redirect('userprofile:main-profile-page', id=user.id)
    else:
        pass

    context = {
        'form': form,
    }
    return render(request, 'userprofile/edit_profile.html', context)