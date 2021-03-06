# Generated by Django 2.2.2 on 2019-06-11 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badball', '0077_auto_20190610_1854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livestat',
            old_name='x_avg',
            new_name='avg',
        ),
        migrations.RenameField(
            model_name='livestat',
            old_name='x_avg_diff',
            new_name='babip',
        ),
        migrations.RenameField(
            model_name='livestat',
            old_name='x_slg',
            new_name='obp',
        ),
        migrations.RenameField(
            model_name='livestat',
            old_name='x_slg_diff',
            new_name='slg',
        ),
        migrations.RemoveField(
            model_name='livestat',
            name='x_woba',
        ),
        migrations.RemoveField(
            model_name='livestat',
            name='x_woba_diff',
        ),
        migrations.AddField(
            model_name='livestat',
            name='hr',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='livestat',
            name='sb',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
