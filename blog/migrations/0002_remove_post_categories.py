# Generated by Django 3.2.6 on 2021-08-13 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
    ]
