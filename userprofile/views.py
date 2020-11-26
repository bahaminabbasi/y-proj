from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from accounts.models import User

@login_required
def main_profile_page(request, id):
    user = User.objects.filter(pk=id).first()
    return render(request, 'userprofile/main_profile_page.html', {'user': user})