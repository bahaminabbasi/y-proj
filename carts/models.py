from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed
import persian

from products.models import Product
from A.utils import shamsi_date

User = settings.AUTH_USER_MODEL



class OrderManager(models.Manager):
    def new_or_get(self, request):
        if request.user.is_authenticated:
            user = request.user
            order_obj, created = Order.objects.get_or_create(user=user, status='pending')
            # print('session order id', request.session['order_id'])
            session_order_id = request.session.get('order_id', None)
            if session_order_id is not None:
                qs = self.get_queryset().filter(id=session_order_id)
                session_order_obj = qs.first()
                print('order in session, obj: ', session_order_obj)
                if session_order_obj is not None:
                    session_items = session_order_obj.orderitem_set.all()
                    items = order_obj.orderitem_set.all()
                    for session_item in session_items:
                        found = False
                        for item in items:
                            if item.product.english_title == session_item.product.english_title:
                                found = True
                                item.quantity = item.quantity + session_item.quantity
                                if item.quantity > item.product.quantity:
                                    item.quantity = item.product.quantity
                                item.save()
                        if not found:
                            session_item.order = order_obj
                            session_item.save()
                    request.session.pop('order_id')
                    session_items.delete()
                    session_order_obj.delete()
            # else:
            #     print('session_order_id was None!')   
        else:
            order_obj, created = Order.objects.get_or_create(user=None, status='pending')
            request.session['order_id'] = order_obj.id
        return order_obj, created

    


class Order(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=True, null=True)
    transaction_id = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    reserved = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return persian.convert_en_numbers(total)

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity  for item in orderitems])
        return total

    objects = OrderManager()

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.english_title} {self.quantity} for {self.order}'

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total



















# class CartManager(models.Manager):
#     def new_or_get(self, request):
#         cart_id = request.session.get('cart_id', None)
#         qs = self.get_queryset().filter(id=cart_id)
#         if qs.count() == 1:
#             new_obj = False
#             print('Cart id exists')
#             cart_obj = qs.first()
#             if request.user.is_authenticated and cart_obj.user is None:
#                 cart_obj.user = request.user
#                 cart_obj.save()
#         else:
#             cart_obj = Cart.objects.new(user=request.user)
#             new_obj = True
#             request.session['cart_id'] = cart_obj.id
#         return cart_obj, new_obj


#     def new(self, user=None):
#         user_obj = None
#         if user is not None:
#             if user.is_authenticated:
#                 user_obj = user     
#         return self.model.objects.create(user=user_obj)


# class Cart(models.Model):
#     user            = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
#     products        = models.ManyToManyField(Product, blank=True)
#     subtotal        = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
#     total           = models.IntegerField()
#     updated         = models.CharField(max_length=160, default=shamsi_date)
#     timpestamp      = models.CharField(max_length=160, default=shamsi_date)

#     objects = CartManager()

#     def __str__(self):
#         return str(self.id)

#     def persian_total_price(self):
#         return persian.convert_en_numbers(self.total)

#     def persian_subtotal_price(self):
#         return persian.convert_en_numbers(self.subtotal)


# def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
#     if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
#         products = instance.products.all()
#         total = 0
#         for x in products:
#             total += x.price
#         if instance.subtotal != total:
#             instance.subtotal = total
#             instance.save()

# m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)


# def pre_save_cart_receiver(sender, instance, *args, **kwargs):
#     if instance.subtotal > 0:
#         instance.total = instance.subtotal + 0
#     else:
#         instance.total = 0.00   

# pre_save.connect(pre_save_cart_receiver, sender=Cart)

