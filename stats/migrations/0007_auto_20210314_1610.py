# Generated by Django 3.1.7 on 2021-03-14 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0006_auto_20210314_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
