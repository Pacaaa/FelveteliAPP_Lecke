# Generated by Django 3.2.12 on 2022-04-01 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0005_auto_20220401_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diak',
            name='diakigazolvanyszam',
        ),
        migrations.RemoveField(
            model_name='diak',
            name='diakneve',
        ),
        migrations.RemoveField(
            model_name='diak',
            name='elertpontszam',
        ),
        migrations.RemoveField(
            model_name='diak',
            name='felvetteke',
        ),
    ]
