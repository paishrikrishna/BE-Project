# Generated by Django 2.2.16 on 2021-02-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_page', '0003_auto_20210215_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='login_model',
            name='email',
            field=models.TextField(default='n/a'),
        ),
        migrations.AddField(
            model_name='login_model',
            name='flat',
            field=models.TextField(default='n/a'),
        ),
        migrations.AddField(
            model_name='login_model',
            name='floor',
            field=models.TextField(default='n/a'),
        ),
        migrations.AddField(
            model_name='login_model',
            name='wing',
            field=models.TextField(default='n/a'),
        ),
    ]
