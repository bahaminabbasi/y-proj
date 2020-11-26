from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from random import randint
from kavenegar import *

### request.session.get['filan'] ###

from .utils import send_message, random_number_generator
from A.secret import api

from .forms import (
            UserLoginForm, 
            PhoneCheckMessage, 
            PhoneNumberConfirm, 
            ChangePassword,
            SetPassword,
            )

from .models import User

# 6E614C3133476C465856332B686151696E332B6C6651722F4D5A424E47647559464D2F6D386477304A424D3D

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')
            password = form.cleaned_data.get('password')
            user = authenticate(request, phone_number=phone_number, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'به یاس دارو خوش آمدید', 'success')
                return redirect('main:home')
            else:
                messages.error(request, 'شماره موبایل یا رمز عبور اشتباه است!', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form':form})


def user_logout(request):
    logout(request)
    # messages.success(request, 'you logged out successfully', 'success')
    return redirect('main:home')


def phone_check_message(request): #### just send sms, set password handels registration
    if request.method == 'POST':
        form = PhoneCheckMessage(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')
            phone_number = '0' + str(phone_number)
            rand_num = random_number_generator()
            request.session['phone_number'] = phone_number
            request.session['code'] = rand_num
            message = 'به یاس دارو خوش آمدید '
            send_message(phone_number, message, rand_num)
            messages.success(request, 'کد ارسال شده را وارد نمایید.', 'success')
            return redirect('accounts:confirm')
    else:
        form = PhoneCheckMessage()
    return render(request, 'accounts/phone_check_message.html', {'form':form})


def phone_confirm(request):
    phone_number = request.session['phone_number']
    if request.method == 'POST':
        code = request.session['code']
        form = PhoneNumberConfirm(request.POST)
        if form.is_valid():
            confirm_code = form.cleaned_data.get('confirm_code')
            if code == confirm_code:
                # messages.success(request, 'حالا رمز عبور', 'success')
                return redirect('accounts:set-password-register')
            else:
                messages.success(request, 'کد اشتباه است!', 'danger')
                return redirect('accounts:confirm')
    else:
        form = PhoneNumberConfirm()
    context =  {
        'form':form,
        'phone_number':phone_number
        }
    return render(request, 'accounts/phone_confirm.html', context)


def set_password_register(request):
    if request.method == 'POST':
        form = SetPassword(request.POST) # set pass
        if form.is_valid():
            phone_number = request.session['phone_number']
            password = form.cleaned_data.get('password1')
            # print(phone_number)
            user = User.objects.create_user(phone_number, password)
            user.save()
            messages.success(request, 'با موفقیت در یاس دارو عضو شدید! حالا می توانید وارد شوید.', 'success')
            return redirect('accounts:login')
    else:
        form = SetPassword()
    return render(request, 'accounts/set_password.html', {'form':form})


def change_password_phone(request):
    if request.method == 'POST':
        form = ChangePassword(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')
            phone_number = '0' + str(phone_number)
            rand_num = random_number_generator()
            request.session['phone_number'] = phone_number
            request.session['code'] = rand_num
            message = 'کد جهت بازیابی رمز عبور '
            send_message(phone_number, message, rand_num)
            return redirect('accounts:change-password-confrim')
    else:
        form = ChangePassword()
    return render(request, 'accounts/change_password.html', {'form':form})


def change_password_confrim(request):
    if request.method == 'POST':
        code = request.session['code']
        form = PhoneNumberConfirm(request.POST)
        if form.is_valid():
            confirm_code = form.cleaned_data.get('confirm_code')
            if code == confirm_code:
                return redirect('accounts:set-new-password')
            else:
                messages.success(request, 'کد اشتباه است!', 'danger')
                return redirect('accounts:change-password-confrim')
    else:
        form = PhoneNumberConfirm()
    return render(request, 'accounts/phone_confirm.html', {'form': form})


def set_new_password(request):
    if request.method == 'POST':
        form = SetPassword(request.POST)
        if form.is_valid():
            phone_number = request.session['phone_number']
            password = form.cleaned_data.get('password1')
            u = User.objects.get(phone_number=phone_number)
            u.set_password(password)
            u.save()
            return redirect('accounts:login')
    else:
        form = SetPassword()
    return render(request, 'accounts/set_new_password.html', {'form': form})