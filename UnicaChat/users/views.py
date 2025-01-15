from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def register_view(request):
    if request.method == "GET":  
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        confirma_senha = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        first_name = str(first_name).title        
        last_name = str(last_name).title
        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('ESSE NOME DE USUARIO JÁ ESTÁ EM USO.')

        if senha != confirma_senha:
            return HttpResponse('SENHAS NÃO CONDIZEM')

        user = User.objects.create_user(username=username, email=email, password=senha, first_name=first_name, last_name=last_name)
        user.save()

        return HttpResponse('USUARIO CADASTRADO COM SUCESSO.')

def login_view(request):
    if request.method == "GET":  
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)

            return(HttpResponse('Usuario autenticado.'))
        else:
            return(HttpResponse('Username ou Senha inválidos!'))
