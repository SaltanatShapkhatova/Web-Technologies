# Generated by Django 2.0.3 on 2018-04-19 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='repeated_password',
        ),
    ]