# Generated by Django 2.0.8 on 2018-12-05 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ulmg', '0060_auto_20181205_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='season',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
