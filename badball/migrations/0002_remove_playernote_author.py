# Generated by Django 2.0.2 on 2018-02-02 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badball', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playernote',
            name='author',
        ),
    ]
