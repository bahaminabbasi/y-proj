from django import forms

from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['first_name'].required = True
        for field in self:
            field.field.widget.attrs['class'] = 'form-control'
            field.field.required = True
            print(field)
    class Meta:
        model = UserProfile
        exclude = ['user_name', ]
        widgets = {
            'first_name': forms.TextInput(attrs={'cols': 1, 'rows': 1}),
        }
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
        }