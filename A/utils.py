import datetime
import string
import random
from django.utils.text import slugify

from .dateconverter import shamsiDate

def shamsi_date():
    now    = datetime.datetime.now()
    year   = now.year
    month  = now.month
    day    = now.day
    hour   = now.hour
    minute = now.minute
    second = now.second
    if len(str(day)) == 1:
        day = "0" + str(day)
    if len(str(month)) == 1:
        month = "0" + str(month)
    if len(str(minute)) == 1:
        minute = "0" + str(minute)
    if len(str(second)) == 1:
        second = "0" + str(second)
    stoday   = shamsiDate(int(year), int(month), int(day))
    clocknow = str(hour) +":"+ str(minute) +":"+ str(second)
    return f'{stoday} - {clocknow}'


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.english_title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
    

    