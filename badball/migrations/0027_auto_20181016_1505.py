# Generated by Django 2.0.8 on 2018-10-16 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ulmg', '0026_auto_20181015_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerpositionyearrating',
            name='player',
        ),
        migrations.RemoveField(
            model_name='roster',
            name='team',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='mascot',
            new_name='nickname',
        ),
        migrations.RemoveField(
            model_name='player',
            name='roster',
        ),
        migrations.DeleteModel(
            name='PlayerPositionYearRating',
        ),
        migrations.DeleteModel(
            name='Roster',
        ),
    ]