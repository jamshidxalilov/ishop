# Generated by Django 3.1.7 on 2021-03-27 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_auto_20210324_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
