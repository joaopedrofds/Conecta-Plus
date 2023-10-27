from django.shortcuts import render, redirect
from django.http.response import HttpResponse 
from .form import CadastroForm
from .models import Voluntario


def teste(request):
    
    return render(request, 'paginas/teste.html')

def pagina_inicial(request):
    return render(request, 'paginas/home.html')

def projetos(request):
    return render(request, 'paginas/projetos.html')

def caçadores(request):
    return render(request, 'paginas/caçadores.html')

def inicio(request):
    return render(request, 'paginas/inicio.html')

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        
        if form.is_valid():
            form.save()
    
            return redirect('login')
    else:
        form = CadastroForm()
        
    return render(request, 'paginas/cadastro.html', {
        'form': form
    })

def voluntarios(request):
    voluntarios = Voluntario.objects.all()
    context = {'voluntarios': voluntarios}
    return render(request, 'paginas/voluntarios.html', context)

