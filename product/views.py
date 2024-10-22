from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

# Create your views here.
class ProductList(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('Lista de produtos')

class Detail(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhes do produto')

class AddToCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adicionar ao carrinho')

class RemoveToCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover do carrinho')

class Cart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')

class Finish(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar Pedido')
