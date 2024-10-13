from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse
from .forms import CustomUserCreationForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('workshop_list')  # Alteração aqui
    else:
        form = CustomUserCreationForm()
    
    context = {
        'form': form,
        'title': 'Cadastrar',
    }
    return render(request, 'accounts/signup.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('workshop_list')
            else:
                messages.error(request, 'Email ou senha inválidos.')
    else:
        form = LoginForm()
    
    context = {
        'form': form,
        'title': 'Login',
    }
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('workshop_list')