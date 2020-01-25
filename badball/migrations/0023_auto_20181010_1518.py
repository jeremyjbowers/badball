# Generated by Django 2.0.8 on 2018-10-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ulmg', '0022_auto_20181010_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_carded',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='level',
            field=models.CharField(choices=[('V', 'V'), ('A', 'A'), ('B', 'B')], max_length=255, null=True),
        ),
    ]