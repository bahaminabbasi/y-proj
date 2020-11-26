from django.db import models

GENDER = [
    ('MALE', 'آقایان'),
    ('FEMALE', 'خانمها'),
    ('BOTH', 'عمومی'),
]


class Category(models.Model):
    name                = models.CharField(max_length=50, unique=True)
    slug                = models.SlugField(max_length=60)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    parent              = models.ForeignKey(Category, models.SET_NULL, null=True, blank=True)
    sub_parent          = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    name                = models.CharField(max_length=150)
    slug                = models.SlugField(max_length=60)
    nesting_level       = models.PositiveIntegerField(default=2, blank=True, null=True)


    def __str__(self):
        return self.name


class StandardDescription(models.Model):
    made_in             = models.CharField(max_length=200)
    gender              = models.CharField(max_length=10, choices=GENDER, default='BOTH')
    form                = models.CharField(max_length=100)
    pack_of             = models.CharField(max_length=100)
    dosage              = models.TextField()
    usage               = models.TextField()
    short_description   = models.TextField(default='')
    features            = models.TextField(default='')
    storing             = models.TextField()

    def __str__(self):
        return self.made_in