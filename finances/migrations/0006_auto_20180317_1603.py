# Generated by Django 2.0 on 2018-03-17 16:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0005_auto_20180317_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typeexpense',
            name='rank',
        ),
        migrations.AddField(
            model_name='typeexpense',
            name='importance',
            field=models.PositiveSmallIntegerField(default=5, help_text='How much is important this expense for you. Min:1 - Max:10', validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
