from django.db import models

from userprofile.models import UserProfile


class Address(models.Model):
    user_name              = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE)
    state                  = models.CharField(max_length=120)
    city                   = models.CharField(max_length=120)
    full_address           = models.TextField()
    plaque                 = models.CharField(max_length=120, null=True, blank=True)
    flat                   = models.CharField(max_length=120, null=True, blank=True)
    postal_code            = models.CharField(max_length=120)
    receiver_firstname     = models.CharField(max_length=120, null=True, blank=True)
    receiver_lastname      = models.CharField(max_length=120, null=True, blank=True)
    receiver_phone         = models.CharField(max_length=120, null=True, blank=True)


    def __str__(self):
        return f'{self.receiver_firstname} {self.receiver_lastname} {self.city}'