from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse

from products.models import Product
from .models import Order, OrderItem


def cart_home(request):

    order, created  = Order.objects.new_or_get(request)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    # # context = {'cart': cart_obj}

    return render(request, 'carts/store.html', context)


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            prodcut_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print('show message to user, product is gone!')
            return redirect('carts:home')
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if prodcut_obj in cart_obj.products.all():
            cart_obj.products.remove(product_id) # removed should be removed and plus one should be implemented
        else:
            cart_obj.products.add(prodcut_obj)
    return redirect('carts:home')

def maxlimit(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        counterPro = int(request.POST['counterPro'])
        product = get_object_or_404(Product, pk=product_id)
        if product.quantity - 2 <= counterPro:
            return JsonResponse({'status':'ok'})
        else:
            return JsonResponse({'status':'notOk'})


def updateItem(request):
    if request.method == 'POST':
        productId = request.POST['productId']
        action = request.POST['action']
        print(productId, action)

        max_reached = 'no'
        # user = request.user
        product = Product.objects.get(id=productId)

        quantity = product.quantity

        order, created = Order.objects.new_or_get(request)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        orderitem_quantity = orderItem.quantity

        if action == 'add' and orderitem_quantity < quantity:
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'add' and orderitem_quantity >= quantity:
            max_reached = 'yes'
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()
    return JsonResponse({'max_reached': max_reached})