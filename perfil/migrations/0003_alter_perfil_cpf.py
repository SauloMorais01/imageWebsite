# Generated by Django 5.1.2 on 2024-10-18 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_perfil_first_name_perfil_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='cpf',
            field=models.CharField(help_text='Cadastro de Pessoa Fisica', max_length=11, verbose_name='CPF'),
        ),
    ]
