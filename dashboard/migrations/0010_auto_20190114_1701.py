# Generated by Django 2.1.5 on 2019-01-14 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserModel',
        ),
    ]
