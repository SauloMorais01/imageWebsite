from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

# Create your views here.
class Pay(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar')

class CloseOrder(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Fechar Pedido')

class Detail(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')
