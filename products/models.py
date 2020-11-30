from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from imagekit.models import ImageSpecField
from pilkit.processors import Thumbnail
import persian

from iteminfo.models import Category, SubCategory, StandardDescription
from A.utils import shamsi_date, unique_slug_generator



class Product(models.Model):
    english_title       = models.CharField(max_length=200)
    persian_title       = models.CharField(max_length=200)
    brand_name          = models.CharField(max_length=200)
    price               = models.DecimalField(decimal_places=0, max_digits=30, default=100000)
    quantity            = models.PositiveIntegerField(default='1')
    slug                = models.SlugField(max_length=250, blank=True, null=True)
    active              = models.BooleanField(default=True)
    featured            = models.BooleanField(default=False)
    image               = models.ImageField(upload_to='products_pics', null=True, blank=True)
    date                = models.CharField(max_length=200, default=shamsi_date)
    category            = models.ForeignKey(Category, models.SET_NULL, null=True, blank=True)
    sub_category        = models.ForeignKey(SubCategory, models.SET_NULL, null=True, blank=True)
    description         = models.ForeignKey(StandardDescription, models.SET_NULL, null=True, blank=True)

    image_medium = ImageSpecField(source='image',
                                  processors=[Thumbnail(120, 120)],
                                  format='JPEG',
                                  options={'quality': 60})
    image_small = ImageSpecField(source='image',
                                 processors=[Thumbnail(50, 50)],
                                 format='JPEG',
                                 options={'quality': 60})

    #quantity caterody

    def __str__(self):
        return self.english_title

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

    def persian_num(self):
        # i = 0
        # result = ''
        # for num in reversed(persian.convert_en_numbers(self.price)):
        #     print(num)
        #     if i == 2:
        #         result = num + ',' +result
        #     else:
        #         result = num + result
        #     i += 1

        return persian.convert_en_numbers(self.price)



def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Product)
