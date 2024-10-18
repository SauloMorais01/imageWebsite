from django.db import models

from PIL import Image
import os

from django.conf import settings

from utils.random_number_generator import random_number_generator
from utils.format_price import format_price
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="nome")
    theme = models.CharField(
        default="none",
        max_length=30,
        choices=(
            ("none", "Sem tema especifico"),
            ("Hallowen", "Tema de hallowen"),
            ("Natal", "Tema de Natal"),
            ("AnoNovo", "Tema de Ano novo"),
        ),
        verbose_name="Tema",
    )
    shot_description = models.TextField(max_length=255, verbose_name="Descrição curta")
    long_description = models.TextField(verbose_name="Descrição longa")
    image = models.ImageField(upload_to='product_image/%Y/%m/%d/', blank=True, null=True, verbose_name="Imagem" )
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="Código")
    marketing_price = models.FloatField(default=0, verbose_name="Preço")
    promotional_price = models.FloatField(default=0, verbose_name="Preço promocional")
    type = models.CharField(
        default="Aberto",
        max_length=30,
        choices=(
            ("Aberto", "Pack com imagens separadas"),
            ("Fechado", "Pack com imagens Finalizadas"),
        ),
        verbose_name="Tipo"
    )
    stockPerPurchase = models.PositiveIntegerField(default=10, verbose_name="Quantidade de downloads por compra")

    def get_price_formater(self):
        return f'R$: {format_price(self.marketing_price)}'
    get_price_formater.short_description = "Preço"

    def get_promotinal_price_formater(self):
        return f'R$: {format_price(self.promotional_price)}'
    get_promotinal_price_formater.short_description = "Preço Promocional"

    @staticmethod
    def resize_image(img, new_width=500):
        img_full_path = settings.MEDIA_ROOT / img.name
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        random_number = random_number_generator(4)
        random_number2 = random_number_generator(4)
        random_number3 = random_number_generator(4)
        if not self.slug:
            slug = f'{slugify(self.name)}-{random_number}-{random_number2}-{random_number3}'
            self.slug = slug


        super().save(*args, **kwargs)

        max_image_size = 500

        if self.image:
            self.resize_image(self.image, max_image_size)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="produto"
        verbose_name_plural="produtos"

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Produto")
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Nome")
    price = models.FloatField(verbose_name="Preço")
    promotional_price_variation = models.FloatField(default=0, verbose_name="Preço Promocional")
    stock = models.PositiveIntegerField(default=1, verbose_name="Estoque")

    def __str__(self):
        return self.name or self.product.name
    
    class Meta:
        verbose_name="Variação"
        verbose_name_plural="Variações"
