# Generated by Django 3.0.8 on 2020-12-20 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0004_auto_20201212_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='plaque',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(max_length=120),
        ),
    ]
