from carts.models import Order


def general_context(request):
    cart_obj, new_obj = Order.objects.new_or_get(request)
    return {
                'cart': cart_obj,
            }