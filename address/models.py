from django.db import models

from userprofile.models import UserProfile


class Address(models.Model):
    user_name              = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE)
    state                  = models.CharField(max_length=120)
    city                   = models.CharField(max_length=120)
    full_address           = models.CharField(max_length=120)
    postal_code            = models.IntegerField()
    receiver               = models.CharField(max_length=120)
    receiver_phone         = models.CharField(max_length=120)


    def __str__(self):
        return f'{self.receiver} {self.city}'