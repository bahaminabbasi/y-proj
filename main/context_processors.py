from carts.models import Cart

def general_context(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return {
                'cart': cart_obj,
            }