# Generated by Django 2.1.5 on 2019-01-15 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_auto_20190114_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='photo',
            field=models.ImageField(default='../oneOnOne/static/images/android-desktop.png', upload_to='images'),
        ),
    ]
