# Generated by Django 3.0.6 on 2022-09-08 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.TextField(max_length=100)),
                ('files', models.FilePathField(path='users_files')),
            ],
        ),
    ]
