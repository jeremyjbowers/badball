# Generated by Django 2.2.2 on 2019-07-30 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badball', '0084_player_ls_is_mlb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draftpick',
            name='overall_pick_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='draftpick',
            name='pick_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
