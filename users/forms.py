from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import User

class LogInForm(forms.Form):
    Usuario = forms.CharField(max_length=20)
    Contraseña = forms.CharField(max_length=20, widget=forms.PasswordInput())


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'rol',
            'password1',
            'password2',
            'mobil',
            'phone',
            'address',
            'city',
            'zip_code',
            'avatar'
        )
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electronico',
            'rol': 'Tipo de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
