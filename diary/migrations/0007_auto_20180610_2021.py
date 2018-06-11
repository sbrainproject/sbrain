# Generated by Django 2.0 on 2018-06-10 20:21

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0006_smallnote_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dedication',
            name='comment',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='smallnote',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
    ]