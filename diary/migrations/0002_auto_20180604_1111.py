# Generated by Django 2.0 on 2018-06-04 11:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='stars',
            field=models.PositiveSmallIntegerField(default=3, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='date',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='dedication',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='role',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='smallnote',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='typededication',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='typetask',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
    ]
