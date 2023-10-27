from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Voluntario


def teste(request):
    
    return render(request, 'paginas/teste.html')

def pagina_inicial(request):
    return render(request, 'paginas/home.html')

def projetos(request):
    return render(request, 'paginas/projetos.html')

def caçadores(request):
    return render(request, 'paginas/caçadores.html')

def voluntarios(request):
    voluntarios = Voluntario.objects.all()
    context = {'voluntarios': voluntarios}
    return render(request, 'paginas/voluntarios.html', context)