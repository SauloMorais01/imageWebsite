from django.db import models
from django.contrib.auth.models import User

import re

from django.forms import ValidationError

from utils.cpf_validator import cpf_validator

# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nome')
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Sobrenome')
    age = models.PositiveIntegerField(verbose_name="Idade")
    Date_and_birth = models.DateField(verbose_name="Data de nascimento")
    cpf = models.CharField(max_length=11, help_text="Cadastro de Pessoa Fisica", verbose_name="CPF")

    def clean(self):
        error_messages = {}

        if not cpf_validator(self.cpf):
            error_messages['cpf'] = 'Digite um CPF válido!'

        if error_messages:
            raise ValidationError(error_messages)


    def __str__(self):
        return f'Perfil de {self.first_name} {self.last_name}' or self.user
    
    class Meta:
        verbose_name='Perfil'
        verbose_name_plural='Perfis'


class Address(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, verbose_name='Perfil')
    address = models.CharField(max_length=50, verbose_name='Endereço')
    number = models.CharField(max_length=5, verbose_name='Número')
    complement = models.CharField(max_length=30, verbose_name='Complemento')
    neighborhood = models.CharField(max_length=30, verbose_name='Bairro')
    cep = models.CharField(max_length=8, verbose_name='CEP')
    city = models.CharField(max_length=30, verbose_name='Cidade')
    state = models.CharField(
        max_length=2,
        default='SP',
        choices=(
            ('AC',  'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RR', 'Roraíma'),
            ('RO', 'Rondônia'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        ),
        verbose_name='Estado'
    )

    def clean(self):
        error_messages = {}
        if re.search(r'[^0-9]', self.cep) or len(self.cep) < 8:
            error_messages['cep'] = 'Digite um cep válido'

        if error_messages:
            raise ValidationError(error_messages)

    def __str__(self):
        return f'Endereço de {self.perfil.first_name} {self.perfil.last_name}' or Perfil.user

    class Meta:
        verbose_name='Endereço'
        verbose_name_plural='Endereços'
