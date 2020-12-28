from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
import os

from .forms import AddProductForm, SubCategoryForm, CategoryForm, StandardDescriptionForm, MainPicturesForm
from products.models import Product
from iteminfo.models import Category, SubCategory, StandardDescription
from main.models import MainPictures
from picture.models import Picture


@staff_member_required
def dashboard_home(request):
    return render(request, 'dashboard/home.html')


@staff_member_required
def add_product(request):
    categories = Category.objects.all()
    des_form = StandardDescriptionForm()
    context = {
        'des_form': des_form,
        'categories': categories,
    }
    if request.method == 'POST':
        print('POST: ', request.POST)
        print('FILES: ', request.FILES)

        persian_title = request.POST.get('persianTitle')
        english_title = request.POST.get('englishTitle')
        brand_name = request.POST.get('brand_name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        cat = request.POST.get('select_categories')
        sub_cat1 = request.POST.get('levelone_placeholder')
        sub_cat2 = request.POST.get('leveltwo_placeholder')
        sub_cat3 = request.POST.get('levelthree_placeholder')
        image = request.FILES['image']

        print()
        print(sub_cat1, sub_cat2, sub_cat3)
        print()
        category = Category.objects.filter(name=cat).first()
        if sub_cat3 != '-------------':
            sub_cat3_obj = SubCategory.objects.filter(name=sub_cat3).first()
            sub_category = sub_cat3_obj
        elif sub_cat2 != '-------------':
            sub_cat2_obj = SubCategory.objects.filter(name=sub_cat2).first()
            sub_category = sub_cat2_obj
        
        elif sub_cat1 != '-------------':
            sub_cat1_obj = SubCategory.objects.filter(name=sub_cat1).first()
            sub_category = sub_cat1_obj
        des_form = StandardDescriptionForm(request.POST)
        if des_form.is_valid():
            description = des_form.save()
        
        b = Product(
                    persian_title=persian_title, 
                    english_title=english_title, 
                    brand_name=brand_name,
                    price=price, quantity=quantity,
                    image=image,
                    category=category,
                    sub_category=sub_category,
                    description = description,
                    )
        b.save()
        image_1 = request.FILES['image_1']
        image_2 = request.FILES['image_2']
        image_3 = request.FILES['image_3']
        p1 = Picture(product=b, image=image_1)
        p2 = Picture(product=b, image=image_2)
        p3 = Picture(product=b, image=image_3)
        p1.save()
        p2.save()
        p3.save()
    else:
        des_form = StandardDescriptionForm()
    return render(request, 'dashboard/add_product.html', context)


@staff_member_required
def tables(request):
    products = Product.objects.all()
    return render(request, 'dashboard/tables.html', {'products': products})


@staff_member_required
def edit_product(request, id):
    product = Product.objects.filter(pk=id).first()
    cat = product.category
    sub_cat = product.sub_category
    categories = Category.objects.all()
    pictures = Picture.objects.filter(product=product)

    context = {
        'product' : product,
        'categories': categories,
        'pictures': pictures,
    }
    if sub_cat is not None:
            if sub_cat.nesting_level == 3:
                sub_cat3 = sub_cat
                sub_cat2 = sub_cat3.sub_parent
                sub_cat1 = sub_cat2.sub_parent
                cat0 = cat
                context['sub_cat3'] = sub_cat3
                context['sub_cat2'] = sub_cat2
                context['sub_cat1'] = sub_cat1
                context['cat0'] = cat0
            elif sub_cat.nesting_level == 2:
                sub_cat2 = sub_cat
                sub_cat1 = sub_cat2.sub_parent
                cat0 = cat
                context['sub_cat2'] = sub_cat2
                context['sub_cat1'] = sub_cat1
                context['cat0'] = cat0
            elif sub_cat.nesting_level == 1:
                sub_cat1 = sub_cat
                cat0 = cat
                context['sub_cat1'] = sub_cat1
                context['cat0'] = cat0
            else:
                context['sub_cat1'] = sub_cat
                context['cat0'] = cat
    
    if request.method == 'POST':
        

        if request.POST['select_categories'] == '-------------':
            edited_cat = cat
            edited_subcat = sub_cat
        else:
            mod_cat = request.POST['select_categories']
            edited_cat = Category.objects.filter(name=mod_cat).first()
            if request.POST['levelthree_placeholder'] != '-------------':
                mod_subcat = request.POST['levelthree_placeholder']
                edited_subcat = SubCategory.objects.filter(name=mod_subcat).first()
            elif request.POST['leveltwo_placeholder'] != '-------------':
                mod_subcat = request.POST['leveltwo_placeholder']
                edited_subcat = SubCategory.objects.filter(name=mod_subcat).first()
            elif request.POST['levelone_placeholder'] != '-------------':
                mod_subcat = request.POST['levelone_placeholder']
                edited_subcat = SubCategory.objects.filter(name=mod_subcat).first()


        persian_title = request.POST.get('persianTitle')
        english_title = request.POST.get('englishTitle')
        brand_name = request.POST.get('brand_name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        category = request.POST.get('category')
        sub_category = request.POST.get('sub_category')
        made_in = request.POST.get('made_in')
        gender = request.POST.get('gender')
        form = request.POST.get('form')
        pack_of = request.POST.get('pack_of')
        dosage = request.POST.get('dosage')
        usage = request.POST.get('usage')
        short_description = request.POST.get('short_description')
        features = request.POST.get('features')
        storing = request.POST.get('storing')
        # image check
        if 'image' in request.POST:
            image = product.image
        else:
            os.remove(product.image.path)
            image = request.FILES['image']
        # making set of pictres in gallery into a ->
        # list so we can tell them apart by indexing
        p_list = []
        for picture in pictures:
            p_list.append(picture)

        # print()
        # print("P_LIST : ", p_list)
        # print()

        image1 = p_list[0]
        image2 = p_list[1]
        image3 = p_list[2]

        # print()
        # print("P_LIST images2 : ", p_list[1].image)
        # print()

        # checking which images are altered, but not removing old ones!
        if 'image1' in request.POST:
            image1 = image1.image
            # print()
            # print("after if : ", image1)
            # print()
        else:
            image1 = request.FILES['image1']
            print()
            print("after else : ", image1)
            print()
        if 'image2' in request.POST:
            image2 = image2.image
        else:
            image2 = request.FILES['image2']
        if 'image3' in request.POST:
            image3 = image3.image
        else:
            image3 = request.FILES['image3']

        product.persian_title = persian_title
        product.english_title = english_title
        product.brand_name = brand_name
        product.price = price
        product.quantity = quantity
        product.image = image
        product.description.made_in = made_in
        product.description.gender = gender
        product.description.form = form
        product.description.pack_of = pack_of
        product.description.dosage = dosage
        product.description.usage = usage
        product.description.short_description = short_description
        product.description.features = features
        product.description.storing = storing
        product.category = edited_cat
        product.sub_category = edited_subcat
        product.description.save()
        product.save()
        i = 0
        for picture in pictures:
            if i == 0:
                picture.image = image1 
                picture.save()
                # print(picture.image)
                # print(image1)
            if i == 1:
                picture.image = image2 
                picture.save()
                # print(picture.image)
                # print(image2)
            if i == 2:
                picture.image = image3 
                picture.save()
                # print(picture.image)
                # print(image3)
            i += 1
        return redirect('dashboard:tables')
    else:
        pass
    return render(request, 'dashboard/edit_product.html', context)


@staff_member_required
def delete_product(request, id):
    product = Product.objects.filter(pk=id).first()
    return render(request, 'dashboard/delete_product.html', {'product': product})


@staff_member_required
def delete_product_confirmed(request, id):
    product = Product.objects.filter(pk=id).first()
    os.remove(product.image.path)
    product.delete()
    return redirect('dashboard:tables')


@staff_member_required
def add_main_slider(request):
    form = MainPicturesForm()
    return render(request, 'dashboard/add_main_slider.html', {'form': form})


@staff_member_required
def choose_main_slider(request):
    main_pictures = MainPictures.objects.all()
    return render(request, 'dashboard/choose_main_slider.html', {'main_pictures': main_pictures})


def levelzero_selected(request):
    if request.method == 'POST':
        selected_category = request.POST['selected_category']
        cat_obj = Category.objects.filter(name=selected_category).first()
        levelzero_selected = SubCategory.objects.filter(parent=cat_obj, nesting_level=1)
        result = []
        for levz in levelzero_selected:
            result.append(levz.name)
        return JsonResponse({'result': result})


def levelone_selected(request):
    if request.method == 'POST':
        selected_category_one = request.POST['selected_category_one']
        subcat_obj = SubCategory.objects.filter(name=selected_category_one, nesting_level=1).first()
        levelone_selected = SubCategory.objects.filter(sub_parent=subcat_obj, nesting_level=2)
        result = []
        for levz in levelone_selected:
            result.append(levz.name)
        return JsonResponse({'result': result})


def leveltwo_selected(request):
    if request.method == 'POST':
        selected_category_one = request.POST['selected_category_one']
        print('selected_category_one', selected_category_one)
        subcat_obj = SubCategory.objects.filter(name=selected_category_one, nesting_level=2).first()
        print('subcat_obj', subcat_obj.slug)
        levelone_selected = SubCategory.objects.filter(sub_parent=subcat_obj, nesting_level=3)
        print('levelone_selected', levelone_selected)
        result = []
        for levz in levelone_selected:
            result.append(levz.name)
        print(result)
        return JsonResponse({'result': result})