# Generated by Django 2.1.4 on 2018-12-08 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0015_auto_20181208_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.IncomeType'),
        ),
    ]