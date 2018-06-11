# Generated by Django 2.0 on 2018-06-10 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1)),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]