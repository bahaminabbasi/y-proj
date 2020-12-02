from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL

class UserProfile(models.Model):
    user_name           = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name          = models.CharField(max_length=120, null=True, blank=True)
    last_name           = models.CharField(max_length=120, null=True, blank=True)
    contact_number      = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


def create_profile(sender, instance, *args, **kwargs):
    UserProfile.objects.create(user_name=instance)

post_save.connect(create_profile, sender=User)

