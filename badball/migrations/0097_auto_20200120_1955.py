# Generated by Django 3.0.2 on 2020-01-20 19:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badball', '0096_auto_20200120_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='scouting_reports',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), default=list, size=None),
        ),
    ]
