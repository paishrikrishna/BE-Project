# Generated by Django 2.2.16 on 2020-11-19 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requested_events', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='events',
            new_name='req_events',
        ),
    ]