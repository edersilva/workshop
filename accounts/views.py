from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, LoginForm, UserProfileForm
from .models import UserProfile, CustomUser
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

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

@login_required
def edit_profile(request):
    User = get_user_model()
    user = get_object_or_404(CustomUser, username=request.user.username)
    profile, created = CustomUser.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('profile')  # Redirect to profile page after successful update
    else:
        form = UserProfileForm(instance=profile)

    context = {
        'form': form,
        'title': 'Editar Perfil',
    }
    
    return render(request, 'accounts/edit.html', context)

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = CustomUser.objects.get(email=email)
            # Gerar token único
            token = get_random_string(length=32)
            # Salvar token no perfil do usuário ou em um modelo separado
            user.profile.reset_password_token = token
            user.profile.save()
            
            # Enviar e-mail com link de recuperação
            reset_link = request.build_absolute_uri(
                reverse('reset_password', args=[token])
            )
            send_mail(
                'Recuperação de Senha',
                f'Clique no link para redefinir sua senha: {reset_link}',
                'noreply@seusite.com',
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Um e-mail com instruções foi enviado para você.')
            return redirect('login')
        except CustomUser.DoesNotExist:
            messages.error(request, 'Não existe usuário com este e-mail.')
    
    context = {
        'title': 'Esqueceu sua senha?',
    }
    return render(request, 'accounts/forgot-password.html', context)
