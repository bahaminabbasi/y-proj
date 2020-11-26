from django import forms
from django.forms import TextInput, Select

from products.models import Product
from iteminfo.models import Category, SubCategory, StandardDescription
from main.models import MainPictures


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ['slug', 'active', 'date', 'category', 'description']
        widgets = {
            'english_title': TextInput(attrs={'class':'form-control','cols': 10, 'rows': 1}),
            'persian_title': TextInput(attrs={'class':'form-control','cols': 10, 'rows': 1}),
            'caterody': Select(attrs={'class':'form-control'}),
        }
     


class CategoryForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Category
        exclude = ['slug', 'name']


class SubCategoryForm(forms.ModelForm):
    sub_category = forms.ModelChoiceField(queryset=SubCategory.objects.all())
    class Meta:
        model = SubCategory
        exclude = ['slug', 'parent', 'name']


class StandardDescriptionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self:
            field.field.widget.attrs['class'] = 'form-control'
            
        # self.fields['comment'].widget.attrs.update(size='40')
        # <label for="id_pack_of">Pack of:</label>

    class Meta:
        model = StandardDescription
        fields = '__all__'
        widgets = {
            'dosage': TextInput(attrs={'cols': 10, 'rows': 1}),
            'usage': TextInput(attrs={'cols': 10, 'rows': 1}),
            'short_description': TextInput(attrs={'cols': 10, 'rows': 1}),
            'features': TextInput(attrs={'cols': 10, 'rows': 1}),
            'storing': TextInput(attrs={'cols': 10, 'rows': 1}),
        }
        labels = {
            'made_in': 'کشور سازنده',
            'gender': 'مناسب برای(جنسیت)',
            'form': 'نوع محصول',
            'pack_of': 'سایز',
            'dosage': 'دوز مصرف',
            'usage': 'نحوه مصرف',
            'short_description': 'توضیحات',
            'features': 'ویژگی ها',
            'storing': 'شرایط نگهداری',
        }

class MainPicturesForm(forms.ModelForm):
    class Meta:
        model = MainPictures
        fields = '__all__'
        


# class BookForm(forms.Form):
#     category0 = forms.ModelChoiceField(queryset=Category.objects.filter(parent=None))
#     category1 = forms.ModelChoiceField(queryset=Category.objects.filter(nesting_level=1))
#     category2 = forms.ModelChoiceField(queryset=Category.objects.filter(nesting_level=2))


# class AddCategory(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields ='__all__'
#         exclude = ['slug']
