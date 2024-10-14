from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    total = models.FloatField(verbose_name="Total")
    status = models.CharField(
        default="Criado",
        max_length=15,
        choices= (
            ('Aprovado', 'Aprovado'),
            ('Criado', 'Criado'),
            ('Reprovado', 'Reprovado'),
            ('Pendente', 'Pendente'),
            ('Enviado', 'Enviado'),
            ('Finalizado', 'Finalizado'),
        ),
        verbose_name="Status"
    )

    def __str__(self):
        return f'pedido Nº {self.pk}'

    class Meta:
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'

class OrderItem(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, verbose_name="Pedido")
    product = models.CharField(max_length=255, verbose_name="Produto")
    product_id = models.PositiveIntegerField(verbose_name="Id do produto")
    variation = models.CharField(max_length=255, verbose_name="Variação")
    variation_id = models.PositiveIntegerField(verbose_name="Id da variação")
    price = models.FloatField(verbose_name="Preço")
    promotional_price = models.FloatField(default=0, verbose_name="Preço promocional")
    amount = models.PositiveIntegerField(verbose_name="Quantidade")
    image = models.CharField(max_length=2000, verbose_name="Imagem")

    def __str__(self):
        return f'Item do {self.request}'

    class Meta:
        verbose_name='Item do pedido'
        verbose_name_plural='Itens do pedido'
