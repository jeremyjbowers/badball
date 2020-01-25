# Generated by Django 2.2.2 on 2019-06-10 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badball', '0075_player_js_prospect_rank'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('hitter', models.BooleanField(default=True)),
                ('player_name', models.CharField(blank=True, max_length=255)),
                ('season', models.IntegerField()),
                ('level', models.CharField(blank=True, max_length=255)),
                ('wrc_plus', models.IntegerField(blank=True, null=True)),
                ('plate_appearances', models.IntegerField(blank=True, null=True)),
                ('iso', models.DecimalField(decimal_places=3, max_digits=4)),
                ('k_pct', models.DecimalField(decimal_places=1, max_digits=3)),
                ('bb_pct', models.DecimalField(decimal_places=1, max_digits=3)),
                ('woba', models.DecimalField(decimal_places=3, max_digits=4)),
                ('x_woba', models.DecimalField(decimal_places=3, max_digits=4)),
                ('x_woba_diff', models.DecimalField(decimal_places=3, max_digits=4)),
                ('x_avg', models.DecimalField(decimal_places=3, max_digits=4)),
                ('x_avg_diff', models.DecimalField(decimal_places=3, max_digits=4)),
                ('x_slg', models.DecimalField(decimal_places=3, max_digits=4)),
                ('x_slg_diff', models.DecimalField(decimal_places=3, max_digits=4)),
                ('g', models.IntegerField(blank=True, null=True)),
                ('gs', models.IntegerField(blank=True, null=True)),
                ('era', models.DecimalField(decimal_places=2, max_digits=4)),
                ('fip', models.DecimalField(decimal_places=2, max_digits=4)),
                ('xfip', models.DecimalField(decimal_places=2, max_digits=4)),
                ('siera', models.DecimalField(decimal_places=2, max_digits=4)),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='badball.Player')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
