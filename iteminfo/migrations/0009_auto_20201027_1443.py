# Generated by Django 3.0.8 on 2020-10-27 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iteminfo', '0008_subcategory_sub_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='nesting_level',
            field=models.PositiveIntegerField(blank=True, default=2, null=True),
        ),
    ]
