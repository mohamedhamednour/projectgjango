# Generated by Django 3.2.9 on 2021-12-06 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0009_auto_20211206_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='avg_rate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='projects',
            name='total_donations',
            field=models.IntegerField(),
        ),
    ]
