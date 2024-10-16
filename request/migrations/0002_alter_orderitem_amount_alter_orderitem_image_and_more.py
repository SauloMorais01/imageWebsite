# Generated by Django 5.1.2 on 2024-10-14 01:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='amount',
            field=models.PositiveIntegerField(verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='image',
            field=models.CharField(max_length=2000, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.FloatField(verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.CharField(max_length=255, verbose_name='Produto'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product_id',
            field=models.PositiveIntegerField(verbose_name='Id do produto'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='promotional_price',
            field=models.FloatField(default=0, verbose_name='Preço promocional'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.request', verbose_name='Pedido'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='variation',
            field=models.CharField(max_length=255, verbose_name='Variação'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='variation_id',
            field=models.PositiveIntegerField(verbose_name='Id da variação'),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('Aprovado', 'Aprovado'), ('Criado', 'Criado'), ('Reprovado', 'Reprovado'), ('Pendente', 'Pendente'), ('Enviado', 'Enviado'), ('Finalizado', 'Finalizado')], default='Criado', max_length=15, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='request',
            name='total',
            field=models.FloatField(verbose_name='Total'),
        ),
        migrations.AlterField(
            model_name='request',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
