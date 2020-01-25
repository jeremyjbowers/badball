# Generated by Django 2.0.8 on 2018-10-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ulmg', '0021_player_mlb_prospect_rank'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='owned',
            new_name='is_owned',
        ),
        migrations.RemoveField(
            model_name='player',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='mlb_team',
        ),
        migrations.RemoveField(
            model_name='player',
            name='suffix',
        ),
        migrations.AddField(
            model_name='player',
            name='is_prospect',
            field=models.BooleanField(default=False),
        ),
    ]
