# Generated by Django 2.0 on 2018-06-04 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20180604_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smallnote',
            name='user',
        ),
    ]
