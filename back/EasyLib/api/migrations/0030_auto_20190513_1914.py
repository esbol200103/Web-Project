# Generated by Django 2.2.1 on 2019-05-13 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_auto_20190513_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='api.UserProfile'),
        ),
    ]