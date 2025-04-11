from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django import forms
from django.db import transaction
from .models import Cliente

class ClienteForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = ["username", "password"]

class RegistroForm(UserCreationForm):
    nombre = forms.CharField(max_length=80)
    apellido = forms.CharField(max_length=80)
    email = forms.EmailField()
    nacimiento = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    direccion = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Nombre de usuario',
            'class': 'form-control'
        })

        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Contraseña',
            'class': 'form-control'
        })

        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Repetir contraseña',
            'class': 'form-control'
        })

        self.fields['email'].widget.attrs.update({
            'placeholder': 'Correo electrónico',
            'class': 'form-control'
        })

        self.fields['nombre'].widget.attrs.update({
            'placeholder': 'Nombres',
            'class': 'form-control'
        })

        self.fields['apellido'].widget.attrs.update({
            'placeholder': 'Apellidos',
            'class': 'form-control'
        })

        self.fields['nacimiento'].widget.attrs.update({
            'placeholder': 'Fecha de nacimiento',
            'class': 'form-control'
        })

        self.fields['direccion'].widget.attrs.update({
            'placeholder': 'Dirección',
            'class': 'form-control',
            'rows': 2
        })

    def save(self, commit=True):
        with transaction.atomic():
            user = super().save(commit=False)
            user.email = self.cleaned_data["email"]
            if commit:
                user.save()
                if not Cliente.objects.filter(user=user).exists():
                    Cliente.objects.create(
                        user=user,
                        nombre=self.cleaned_data["nombre"],
                        apellido=self.cleaned_data["apellido"],
                        email=self.cleaned_data["email"],
                        nacimiento=self.cleaned_data["nacimiento"],
                        direccion=self.cleaned_data["direccion"]
                    )
        return user
    
@login_required
def agregar_al_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})

    producto_id_str = str(producto_id)
    if producto_id_str in carrito:
        carrito[producto_id_str] += 1
    else:
        carrito[producto_id_str] = 1

    request.session['carrito'] = carrito
    return redirect('HoneyPanqui:lista_productos')