# Generated by Django 2.2.2 on 2019-06-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ulmg', '0078_auto_20190611_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='livestat',
            name='bb_9',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='livestat',
            name='gb_pct',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='livestat',
            name='hr_9',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='livestat',
            name='hr_fb',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='livestat',
            name='ip',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='livestat',
            name='k_9',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='livestat',
            name='lob_pct',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
    ]
