# Generated by Django 3.2.6 on 2021-08-13 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_postcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomment',
            old_name='commment',
            new_name='comment',
        ),
    ]
