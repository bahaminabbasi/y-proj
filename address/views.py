from django.shortcuts import render, redirect
from django.conf import settings

from .models import Address
from userprofile.models import UserProfile


def add_address(request):
    user = request.user
    if request.method == 'POST':
        user_profile = UserProfile.objects.filter(user_name=user).first()
        state = request.POST.get('state')
        city = request.POST.get('city')
        full_address = request.POST.get('full_address')
        plaque = request.POST.get('plaque')
        flat = request.POST.get('flat')
        postal_code = request.POST.get('postal_code')
        receiver_firstname = request.POST.get('receiver_firstname')
        receiver_lastname = request.POST.get('receiver_lastname')
        receiver_phone = request.POST.get('receiver_phone')
        b = Address(
            user_name=user_profile,
            state=state,
            city=city,
            full_address=full_address,
            plaque=plaque,
            flat=flat,
            postal_code=postal_code,
            receiver_firstname=receiver_firstname,
            receiver_lastname=receiver_lastname,
            receiver_phone=receiver_phone
        )
        b.save()
        context = {
            'active_tab': 'address_tab',
        }
        return render(request, 'userprofile/main_profile_page.html', context)
    else: 
        pass    
    return redirect('userprofile:main-profile-page', id=user.id)