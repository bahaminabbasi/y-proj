# Generated by Django 3.0.8 on 2020-12-02 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_userprofile_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
    ]
