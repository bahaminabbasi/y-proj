# Generated by Django 3.0.8 on 2020-09-26 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iteminfo', '0003_auto_20200926_0759'),
        ('products', '0006_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='iteminfo.SubCategory'),
        ),
    ]
