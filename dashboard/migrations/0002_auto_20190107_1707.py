# Generated by Django 2.1.5 on 2019-01-07 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='blah',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='person',
            name='cat',
            field=models.CharField(default='cat', max_length=250),
        ),
    ]
