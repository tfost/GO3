# Generated by Django 3.1.7 on 2021-03-14 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0005_metric_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='updated',
            field=models.DateTimeField(),
        ),
    ]
