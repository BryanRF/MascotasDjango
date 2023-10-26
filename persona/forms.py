from django import forms
from api.models import Persona, Direccion
from django.contrib.auth.forms import AuthenticationForm
# persona/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioRegistroForm(UserCreationForm):
    email = forms.EmailField()
    nombre = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=15)
    dni = forms.CharField(max_length=15)
    fecha_nacimiento = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'nombre', 'telefono', 'dni', 'fecha_nacimiento']

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'telefono', 'dni', 'email', 'fecha_nacimiento']

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['direccion']

class UsuarioLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
