# Generated by Django 2.2.16 on 2021-02-15 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry_exit_timestamp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry_exit_model',
            old_name='email',
            new_name='number',
        ),
        migrations.RemoveField(
            model_name='entry_exit_model',
            name='flat',
        ),
        migrations.RemoveField(
            model_name='entry_exit_model',
            name='password',
        ),
    ]
