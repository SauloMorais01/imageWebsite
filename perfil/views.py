from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import View
from django.http import HttpResponse


# Create your views here.
class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Entrar')

class SignIn(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Criar')

class Update(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Atualizar')

class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Sair')
