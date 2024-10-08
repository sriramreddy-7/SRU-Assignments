# Generated by Django 5.0 on 2024-09-30 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assigments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(default='')),
                ('subject', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(default='', upload_to='assignments/')),
                ('posted_by', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
