# Generated by Django 2.0.2 on 2018-10-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ulmg', '0023_auto_20181010_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_rostered',
            field=models.BooleanField(default=False),
        ),
    ]
