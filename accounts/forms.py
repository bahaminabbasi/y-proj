from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User # AUTH_USER_MODEL!!!???


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone_number',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('phone_number', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class UserLoginForm(forms.Form):
    phone_number    = forms.IntegerField(label='شماره موبایل',
                                        widget=forms.NumberInput(
                                            attrs={'class':'form-control',
                                            'placeholder':'شماره موبایل خود را وارد نمائید'
                                            }
                                            ))
    password        = forms.CharField(label='رمز عبور', 
                                        widget=forms.PasswordInput(
                                            attrs={'class':'form-control',
                                            'placeholder':'رمز عبور خود را وارد نمایید'
                                            }
                                            ))


class PhoneCheckMessage(forms.Form):
    phone_number    = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        str_phone_number = str(phone_number)
        if len(str_phone_number) != 10:
            raise forms.ValidationError("شماره موبایل معتبر نمی‌باشد.")
        user = User.objects.filter(phone_number=phone_number)
        if user:
            raise forms.ValidationError("این شماره موبایل قبلا ثبت شده است.")
        return phone_number


class PhoneNumberConfirm(forms.Form):
    confirm_code            = forms.IntegerField(widget=forms.NumberInput(
                                        attrs={'class':'form-control', 
                                        'placeholder':'رمز دریافتی به شماره موبایل خود را وارد نمائید'
                                        }
                                        ))


class SetPassword(forms.Form):
    password1 = forms.CharField(label='رمز عبور', 
                                        widget=forms.PasswordInput(
                                            attrs={'class':'form-control',
                                            'placeholder':'رمز عبور خود را وارد نمایید'
                                            }
                                            ))
    password2 = forms.CharField(label='رمز عبور', 
                                        widget=forms.PasswordInput(
                                            attrs={'class':'form-control',
                                            'placeholder':'تکرار رمز '
                                            }
                                            ))

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("رمز عبور و تکرار آن با هم مغایرت دارند")
        return password2


class ChangePassword(forms.Form):
    phone_number    = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        str_phone_number = str(phone_number)
        if len(str_phone_number) != 10:
            raise forms.ValidationError("شماره موبایل معتبر نمی‌باشد")
        user = User.objects.filter(phone_number=phone_number)
        if not user:
            raise forms.ValidationError("شماره موبایل معتبر نمی‌باشد")
        return phone_number



