# Generated by Django 2.2.16 on 2021-02-15 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='entry_exit_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(default='n/a')),
                ('password', models.TextField(default='N/A')),
                ('auth', models.TextField(default='member')),
                ('email', models.TextField(default='n/a')),
                ('wing', models.TextField(default='n/a')),
                ('floor', models.TextField(default='n/a')),
                ('flat', models.TextField(default='n/a')),
            ],
        ),
    ]
