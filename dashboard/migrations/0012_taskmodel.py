# Generated by Django 2.1.5 on 2019-01-14 17:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20190114_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=220)),
                ('creator_name', models.CharField(max_length=120)),
                ('assigned_to', models.CharField(max_length=30)),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]