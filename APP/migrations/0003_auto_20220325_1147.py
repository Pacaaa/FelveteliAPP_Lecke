# Generated by Django 3.2.12 on 2022-03-25 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_auto_20220325_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diak',
            name='diakigazolvanyszam',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='diak',
            name='diakneve',
            field=models.TextField(),
        ),
    ]
