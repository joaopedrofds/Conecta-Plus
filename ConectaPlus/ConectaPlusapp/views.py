from django.shortcuts import render, redirect

# Create your views here.


def teste(request):
    
    return render(request, 'ConectaPlusapp/teste.html')