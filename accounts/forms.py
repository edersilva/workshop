from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, UserProfile
from django.contrib.auth.models import User
from address.models import Address  # Importe o modelo Address

ESTADOS_CHOICES = [
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'),
    ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'),
    ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
    ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'),
    ('SE', 'Sergipe'), ('TO', 'Tocantins')
]

# Definição de estilos comuns
COMMON_FIELD_ATTRS = {
    'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
}

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='Nome', help_text='Obrigatório.')
    last_name = forms.CharField(max_length=30, required=True, label='Sobrenome', help_text='Obrigatório.')
    email = forms.EmailField(max_length=254, required=True, label='Email', help_text='Obrigatório. Informe um endereço de email válido.')
    
    # Campos de endereço
    zipcode = forms.CharField(max_length=10, required=True, label='CEP', help_text='CEP')
    street = forms.CharField(max_length=255, required=True, label='Rua', help_text='Rua')
    neighborhood = forms.CharField(max_length=255, required=True, label='Bairro', help_text='Bairro')
    city = forms.CharField(max_length=255, required=True, label='Cidade', help_text='Cidade')
    number = forms.CharField(max_length=10, required=True, label='Número', help_text='Número')
    complement = forms.CharField(max_length=255, required=False, label='Complemento', help_text='Complemento')
    state = forms.ChoiceField(choices=ESTADOS_CHOICES, required=True, label='Estado', help_text='Estado')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',
                  'zipcode', 'street', 'neighborhood', 'city', 'complement', 'state')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs=COMMON_FIELD_ATTRS))
    password = forms.CharField(widget=forms.PasswordInput(attrs=COMMON_FIELD_ATTRS))

class UserProfileForm(forms.ModelForm):
    zipcode = forms.CharField(max_length=8, required=True)
    state = forms.ChoiceField(choices=ESTADOS_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            # Preencher os campos de endereço
            if hasattr(self.instance, 'address'):
                address = self.instance.address
                self.fields['zipcode'].initial = address.zipcode
                self.fields['state'].initial = address.state
                for field in Address._meta.fields:
                    if field.name not in ['id', 'user', 'zipcode', 'state']:
                        self.fields[field.name] = forms.CharField(required=False)
                        self.initial[field.name] = getattr(address, field.name)

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            address, created = Address.objects.get_or_create(user=user)
            address.zipcode = self.cleaned_data['zipcode']
            address.state = self.cleaned_data['state']
            for field in Address._meta.fields:
                if field.name not in ['id', 'user', 'zipcode', 'state']:
                    setattr(address, field.name, self.cleaned_data.get(field.name))
            address.save()
        return user
