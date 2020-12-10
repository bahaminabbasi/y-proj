from django.shortcuts import render, redirect


def add_address(request):
    return redirect('userprofile:main-profile-page')