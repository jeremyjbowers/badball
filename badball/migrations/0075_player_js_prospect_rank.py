# Generated by Django 2.1.5 on 2019-02-11 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badball', '0074_player_bp_prospect_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='js_prospect_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
