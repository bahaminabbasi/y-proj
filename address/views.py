from django.shortcuts import render, redirect

from .models import Address


def add_address(request):
    user = request.user
    if request.method == 'POST':
        print(request.POST)
        state = request.POST.get('state')
        city = request.POST.get('city')
        full_address = request.POST.get('full_address')
        plaque = request.POST.get('plaque')
        flat = request.POST.get('flat')
        postal_code = request.POST.get('postal_code')
        receiver_firstname = request.POST.get('receiver_name')
        receiver_lastname = request.POST.get('receiver_lastname')
        receiver_phonenumber = request.POST.get('receiver_phonenumber')
        context = {
            'active_tab': 'address_tab',
        }
        return render(request, 'userprofile/main_profile_page.html', context)
    else: 
        pass    
    return redirect('userprofile:main-profile-page', id=user.id)