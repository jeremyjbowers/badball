# Generated by Django 2.0.2 on 2018-02-02 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badball', '0004_auto_20180202_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='owned',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='roster_conflict',
            field=models.BooleanField(default=False),
        ),
    ]
