# Generated by Django 3.2.9 on 2021-12-03 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0002_auto_20211203_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='category',
            field=models.CharField(choices=[('cat1', 'CATEGORY1'), ('cat2', 'CATEGORY2'), ('cat3', 'CATEGORY3'), ('cat4', 'CATEGORY4'), ('cat5', 'CATEGORY5')], default='cat1', max_length=6),
        ),
    ]