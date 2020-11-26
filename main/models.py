from django.db import models


class MainPictures(models.Model):
    # picture
    # date
    # name
    image = models.ImageField(upload_to='general_pictures', null=True, blank=True)
    name = models.CharField(max_length=150)
