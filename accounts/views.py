from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, LoginForm, UserProfileForm
from .models import UserProfile, CustomUser
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from address.models import Address  # Importe o modelo Address
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.backends import ModelBackend

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                user = form.save()
                
                # Criar endereço
                Address.objects.create(
                    user=user,
                    street=request.POST.get('street'),
                    neighborhood=request.POST.get('neighborhood'),
                    city=request.POST.get('city'),
                    number=request.POST.get('number'),
                    complement=request.POST.get('complement'),
                    state=request.POST.get('state'),
                    zipcode=request.POST.get('zipcode')
                )
                
                # Autenticar o usuário
                authenticated_user = authenticate(username=user.username, password=form.cleaned_data['password1'])
                # Fazer login com o backend especificado
                login(request, authenticated_user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, 'Conta criada com sucesso!')
                return redirect('workshop_list')
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
    user = request.user
    address = user.address_set.first()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            with transaction.atomic():
                user = form.save()
                address_data = {
                    'street': form.cleaned_data['street'],
                    'neighborhood': form.cleaned_data['neighborhood'],
                    'city': form.cleaned_data['city'],
                    'number': form.cleaned_data['number'],
                    'complement': form.cleaned_data['complement'],
                    'state': form.cleaned_data['state'],
                    'zipcode': form.cleaned_data['zipcode'],
                }
                if address:
                    for key, value in address_data.items():
                        setattr(address, key, value)
                    address.save()
                else:
                    Address.objects.create(user=user, **address_data)
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('accounts:edit_profile')
    else:
        form = UserProfileForm(instance=user)

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

def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        User = get_user_model()
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Não existe usuário com este e-mail.')
            return render(request, 'accounts/forgot-password.html')
        
        if new_password != confirm_password:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'accounts/reset-password.html')
        
        user.set_password(new_password)
        user.save()
        
        messages.success(request, 'Sua senha foi redefinida com sucesso.')
        return redirect('accounts:login')  # Redireciona para a página de login
    context = { 
        'title': 'Redefinir Senha',
    }
    # Adiciona mensagens de sucesso ou erro ao contexto
    if messages.get_messages(request):
        context['messages'] = messages.get_messages(request)
    return render(request, 'accounts/reset-password.html', context)
