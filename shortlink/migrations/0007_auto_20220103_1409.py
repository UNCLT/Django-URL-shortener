# Generated by Django 3.1.6 on 2022-01-03 11:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortlink', '0006_securelink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='slug',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Slug'),
        ),
    ]
