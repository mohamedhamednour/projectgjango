# Generated by Django 3.2.9 on 2021-12-03 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='category',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]