# Generated by Django 3.0 on 2019-12-27 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20191226_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberpreferences',
            name='email_new_gig',
        ),
    ]
