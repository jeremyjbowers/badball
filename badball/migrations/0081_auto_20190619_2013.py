# Generated by Django 2.2.2 on 2019-06-19 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badball', '0080_auto_20190612_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='is_interesting',
            new_name='is_2h_c',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='bref_name',
            new_name='mlbam_id',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='cbs_id',
            new_name='mlbam_url',
        ),
        migrations.RemoveField(
            model_name='player',
            name='ba_draft_rank',
        ),
        migrations.RemoveField(
            model_name='player',
            name='ba_prospect_rank',
        ),
        migrations.RemoveField(
            model_name='player',
            name='bp_prospect_rank',
        ),
        migrations.RemoveField(
            model_name='player',
            name='cbs_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='cbs_pos',
        ),
        migrations.RemoveField(
            model_name='player',
            name='espn_id',
        ),
        migrations.RemoveField(
            model_name='player',
            name='espn_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='espn_pos',
        ),
        migrations.RemoveField(
            model_name='player',
            name='eta',
        ),
        migrations.RemoveField(
            model_name='player',
            name='fg_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='fg_pos',
        ),
        migrations.RemoveField(
            model_name='player',
            name='fg_prospect_fv',
        ),
        migrations.RemoveField(
            model_name='player',
            name='fg_prospect_rank',
        ),
        migrations.RemoveField(
            model_name='player',
            name='interest_order',
        ),
        migrations.RemoveField(
            model_name='player',
            name='js_prospect_rank',
        ),
        migrations.RemoveField(
            model_name='player',
            name='klaw_prospect_rank',
        ),
        migrations.RemoveField(
            model_name='player',
            name='lahman_id',
        ),
        migrations.RemoveField(
            model_name='player',
            name='mlb_depth',
        ),
        migrations.RemoveField(
            model_name='player',
            name='mlb_id',
        ),
        migrations.RemoveField(
            model_name='player',
            name='mlb_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='mlb_pos',
        ),
        migrations.RemoveField(
            model_name='player',
            name='mlb_prospect_rank',
        ),
        migrations.RemoveField(
            model_name='player',
            name='mlb_team',
        ),
        migrations.RemoveField(
            model_name='player',
            name='mlb_team_long',
        ),
        migrations.RemoveField(
            model_name='player',
            name='mlb_url',
        ),
        migrations.RemoveField(
            model_name='player',
            name='nfbc_id',
        ),
        migrations.RemoveField(
            model_name='player',
            name='nfbc_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='nfbc_pos',
        ),
        migrations.RemoveField(
            model_name='player',
            name='ottoneu_id',
        ),
        migrations.RemoveField(
            model_name='player',
            name='ottoneu_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='ottoneu_pos',
        ),
        migrations.RemoveField(
            model_name='player',
            name='pl_prospect_rank',
        ),
        migrations.RemoveField(
            model_name='player',
            name='retro_id',
        ),
        migrations.RemoveField(
            model_name='player',
            name='retro_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='rotowire_id',
        ),
        migrations.RemoveField(
            model_name='player',
            name='rotowire_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='rotowire_pos',
        ),
        migrations.RemoveField(
            model_name='player',
            name='yahoo_id',
        ),
        migrations.RemoveField(
            model_name='player',
            name='yahoo_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='yahoo_pos',
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
    ]
