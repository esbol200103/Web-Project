# Generated by Django 2.2.1 on 2019-05-09 09:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0011_auto_20190509_1444'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quotation',
            new_name='Review',
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
        migrations.RenameField(
            model_name='review',
            old_name='quotation',
            new_name='text',
        ),
    ]
