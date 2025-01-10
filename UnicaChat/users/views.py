from django.http import HttpResponse
from django.shortcuts import render

def register(request):
    if request.method == "GET":  
        return render(request, 'register.html')
    elif request.method == "POST":
        nome = request.POST.get('username')
        print(nome)
        return HttpResponse('ENVIOU O FORMULARIO')

def login(request):
    return(render(request, 'login.html'))
