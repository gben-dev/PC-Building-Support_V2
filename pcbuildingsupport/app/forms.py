from django import forms
from .models import Ensamble
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EnsambleForm(forms.ModelForm):
    class Meta:
        model = Ensamble
        fields = ['procesador', 'memoria_ram', 'disco_duro', 'tarjeta_video', 'fuente_poder']

class RegistroForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']