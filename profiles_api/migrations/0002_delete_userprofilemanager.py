# Generated by Django 2.2 on 2024-06-16 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfileManager',
        ),
    ]