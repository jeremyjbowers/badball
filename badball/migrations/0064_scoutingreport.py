# Generated by Django 2.1.3 on 2018-12-18 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badball', '0063_auto_20181216_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoutingReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('player_name', models.CharField(blank=True, max_length=255)),
                ('season', models.IntegerField()),
                ('date', models.DateField()),
                ('pv', models.CharField(blank=True, max_length=5, null=True)),
                ('fv', models.CharField(blank=True, max_length=5, null=True)),
                ('risk', models.IntegerField(blank=True, null=True)),
                ('risk_name', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('organization', models.CharField(blank=True, max_length=255, null=True)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('evaluator', models.CharField(blank=True, max_length=255, null=True)),
                ('report_type', models.CharField(blank=True, max_length=255, null=True)),
                ('level', models.CharField(blank=True, max_length=255, null=True)),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='badball.Player')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
