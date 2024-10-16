# Generated by Django 5.1.2 on 2024-10-14 01:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('status', models.CharField(choices=[('Aprovado', 'Aprovado'), ('Criado', 'Criado'), ('Reprovado', 'Reprovado'), ('Pendente', 'Pendente'), ('Enviado', 'Enviado'), ('Finalizado', 'Finalizado')], default='Criado', max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('product_id', models.PositiveIntegerField()),
                ('variation', models.CharField(max_length=255)),
                ('variation_id', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('promotional_price', models.FloatField(default=0)),
                ('amount', models.PositiveIntegerField()),
                ('image', models.CharField(max_length=2000)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.request')),
            ],
            options={
                'verbose_name': 'Item do pedido',
                'verbose_name_plural': 'Itens do pedido',
            },
        ),
    ]
