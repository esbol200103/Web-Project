# Generated by Django 2.2.1 on 2019-05-09 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190509_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='date_of_death',
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]