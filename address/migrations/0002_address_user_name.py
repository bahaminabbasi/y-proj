# Generated by Django 3.0.8 on 2020-12-02 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_remove_userprofile_address'),
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='user_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.UserProfile'),
        ),
    ]
