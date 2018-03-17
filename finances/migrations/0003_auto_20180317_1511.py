# Generated by Django 2.0 on 2018-03-17 15:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0002_creditcard_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditcard',
            name='bill_date',
        ),
        migrations.AddField(
            model_name='creditcard',
            name='bill_day',
            field=models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(31)]),
            preserve_default=False,
        ),
    ]
