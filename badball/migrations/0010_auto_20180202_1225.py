# Generated by Django 2.0.2 on 2018-02-02 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ulmg', '0009_auto_20180202_1041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['abbreviation']},
        ),
        migrations.AddField(
            model_name='player',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='suffix',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
