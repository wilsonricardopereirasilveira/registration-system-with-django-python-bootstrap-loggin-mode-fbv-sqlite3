# Generated by Django 3.1 on 2020-08-21 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0004_funcionario_acessarsistema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='acessarSistema',
            field=models.BooleanField(default=False),
        ),
    ]
