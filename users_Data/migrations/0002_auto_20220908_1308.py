# Generated by Django 3.0.6 on 2022-09-08 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_Data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='test',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='users',
            name='files',
            field=models.FileField(upload_to=''),
        ),
    ]
