# Generated by Django 5.0 on 2024-09-30 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assigments',
            old_name='file',
            new_name='assignment_file',
        ),
    ]
