# Generated by Django 3.0 on 2019-12-27 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='condensed_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='band',
            name='shortname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='band',
            name='hometown',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
