# Generated by Django 3.2.9 on 2021-12-03 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0006_rename_project_name_projects_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='user',
        ),
        migrations.AlterField(
            model_name='projects',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateField(),
        ),
    ]