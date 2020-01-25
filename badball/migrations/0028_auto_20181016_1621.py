# Generated by Django 2.0.8 on 2018-10-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badball', '0027_auto_20181016_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='user',
        ),
        migrations.RemoveField(
            model_name='playernote',
            name='player',
        ),
        migrations.AddField(
            model_name='team',
            name='owner_email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='owner',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Owner',
        ),
        migrations.DeleteModel(
            name='PlayerNote',
        ),
    ]
