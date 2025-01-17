from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def register_view(request):
    if request.method == "GET":  
        return render(request, 'register.html')
    elif request.method == "POST":
        USER = get_user_model()

        ip_address = request.META.get('REMOTE_ADDR')

        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        confirma_senha = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        first_name = str(first_name).title()        
        last_name = str(last_name).title()
        user = USER.objects.filter(username=username).first()

        if user:
            messages.error(request, 'Esse nome de usuário já está em uso!')
            return render(request, 'register.html')

        if senha != confirma_senha:
             messages.error(request, 'As senhas não são iguais. Tente novamente!')
             return render(request, 'register.html')

        user = USER.objects.create_user(username=username, email=email, password=senha, first_name=first_name, last_name=last_name, ip_address=ip_address)
        user.save()

        return redirect("login")

def login_view(request):
    if request.method == "GET":  
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)

            return redirect("home")
        else:
            messages.error(request, 'Username ou Senha inválidos!')
            return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect("login")