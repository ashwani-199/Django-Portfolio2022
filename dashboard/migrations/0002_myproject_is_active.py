# Generated by Django 4.1.2 on 2022-12-12 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myproject',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
