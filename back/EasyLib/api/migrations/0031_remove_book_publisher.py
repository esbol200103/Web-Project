# Generated by Django 2.2.1 on 2019-05-13 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20190513_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
    ]