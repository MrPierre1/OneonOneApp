# Generated by Django 2.1.5 on 2019-01-07 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20190107_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
    ]
