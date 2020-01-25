# Generated by Django 2.0.8 on 2018-10-18 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ulmg', '0032_auto_20181017_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_1h_c',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='is_1h_p',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='is_1h_pos',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='is_2h_c',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='is_2h_p',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='is_2h_pos',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='is_35man_roster',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='is_reserve',
            field=models.BooleanField(default=False),
        ),
    ]