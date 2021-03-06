# Generated by Django 2.2.7 on 2019-12-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badball', '0090_auto_20191228_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='league',
            field=models.CharField(blank=True, choices=[('JPN', 'JPN'), ('KOR', 'KOR'), ('J2', 'J2'), ('TAI', 'TAI'), ('MEX', 'MEX'), ('OTH', 'OTH')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(choices=[('P', 'Pitcher'), ('C', 'Catcher'), ('IF', 'Infield'), ('OF', 'Outfield'), ('IF-OF', 'Infield/Outfield'), ('OF-P', 'Pitcher/Outfield'), ('IF-P', 'Pitcher/Infield')], max_length=255, null=True),
        ),
    ]
