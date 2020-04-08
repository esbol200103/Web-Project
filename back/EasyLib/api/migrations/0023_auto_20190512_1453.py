# Generated by Django 2.2.1 on 2019-05-12 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20190512_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='review',
        ),
        migrations.AddField(
            model_name='review',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='api.Book'),
        ),
    ]