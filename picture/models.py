from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import Thumbnail

from products.models import Product

class Picture(models.Model):
    product         = models.ForeignKey(Product, on_delete=models.CASCADE)
    image           = models.ImageField(upload_to='pictures_gallery')

    image_400 = ImageSpecField(source='image',
                                  processors=[Thumbnail(120, 120)],
                                  format='JPEG',
                                  options={'quality': 60})
    image_small = ImageSpecField(source='image',
                                 processors=[Thumbnail(50, 50)],
                                 format='JPEG',
                                 options={'quality': 60})


    def __str__(self):
        return self.product.english_title