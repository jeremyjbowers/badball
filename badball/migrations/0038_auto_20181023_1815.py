# Generated by Django 2.0.8 on 2018-10-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badball', '0037_draftpick_trade_tradereceipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='draftpick',
            name='draft_round',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='draftpick',
            name='draft_type',
            field=models.CharField(choices=[('aa', 'aa'), ('open', 'open'), ('balance', 'balance')], max_length=255, null=True),
        ),
    ]
