# Generated by Django 3.1 on 2020-08-21 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='profilePicture',
            new_name='profile',
        ),
    ]
