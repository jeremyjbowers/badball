# Generated by Django 2.1.3 on 2018-11-24 14:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badball', '0057_auto_20181124_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='championships',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=4), blank=True, null=True, size=None),
        ),
    ]
