from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class form_bcen(forms.Form):
    modelo = forms.CharField(max_length=40)
    materiales_carcaza = forms.CharField(max_length=40)
    materiales_voluta = forms.CharField(max_length=40)
    presion = forms.IntegerField()
    caudal = forms.IntegerField()
    altura = forms.IntegerField()
    temp = forms.IntegerField()

class form_btor(forms.Form):
    modelo = forms.CharField(max_length=40)
    materiales_carcaza = forms.CharField(max_length=40)
    materiales_tornillo = forms.CharField(max_length=40)
    presion = forms.IntegerField()
    caudal = forms.IntegerField()
    altura = forms.IntegerField()
    temp = forms.IntegerField()

class form_beng(forms.Form):
    modelo = forms.CharField(max_length=40)
    materiales_carcaza = forms.CharField(max_length=40)
    materiales_engranajes = forms.CharField(max_length=40)
    presion = forms.IntegerField()
    caudal = forms.IntegerField()
    altura = forms.IntegerField()
    temp = forms.IntegerField()

class form_registro(UserCreationForm):
    username = forms.CharField(max_length=20, min_length=8,label="Nombre de Usuario")
    password1 = forms.CharField(
        label='Ingrese su contraseña',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=(),
    )
    password2 = forms.CharField(
        label='Ingrese su contraseña nuevamente',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=(),
    )
    email = forms.EmailField(label="Direccion de Email")
    first_name = forms.CharField(max_length=20,label="Nombre")
    last_name = forms.CharField(max_length=20,label="Apellido")

class form_editar(forms.Form):
    email = forms.EmailField(label="Direccion de Email")
    first_name = forms.CharField(max_length=20,label="Nombre")
    last_name = forms.CharField(max_length=20,label="Apellido")
    class meta:
        fields = ['email', 'first_name','last_name']