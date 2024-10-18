from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, UserProfile

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
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    birth_date = forms.DateField(required=True)
    gender = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Feminino')], required=True)
    zip_code = forms.CharField(max_length=8, required=True)
    street = forms.CharField(max_length=255, required=True)
    number = forms.CharField(max_length=10, required=True)
    complement = forms.CharField(max_length=100, required=False)
    neighborhood = forms.CharField(max_length=100, required=True)
    city = forms.CharField(max_length=100, required=True)
    state = forms.ChoiceField(choices=ESTADOS_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',
                  'birth_date', 'gender', 'zip_code', 'street', 'number', 'complement',
                  'neighborhood', 'city', 'state')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(COMMON_FIELD_ATTRS)

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs=COMMON_FIELD_ATTRS))
    password = forms.CharField(widget=forms.PasswordInput(attrs=COMMON_FIELD_ATTRS))

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['birth_date', 'gender', 'street', 'number', 'complement', 'neighborhood', 'city', 'state', 'zip_code']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
