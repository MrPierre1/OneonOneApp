# Generated by Django 2.1.5 on 2019-01-07 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20190107_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='blah',
            new_name='stuff',
        ),
    ]
