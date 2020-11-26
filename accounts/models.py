from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import MyUserManager


class User(AbstractBaseUser):
    phone_number        = models.BigIntegerField(unique=True)
    is_active           = models.BooleanField(default=True)
    is_admin            = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'

    objects = MyUserManager()


    def __str__(self):
        return str(self.phone_number)
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin