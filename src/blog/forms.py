from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Cliente

class ClienteForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = ["username", "password"]

class RegistroForm(UserCreationForm):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField(
                required=True,
        widget=forms.DateInput(attrs={
            'placeholder': 'Fecha de nacimiento',
            'type': 'date',
            'class': 'form-control',
        })
    )
    
    class Meta:
        model = User
        fields = {"username", "password1", "password2"}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.help_text = None

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Nombre de usuario',
            'class': 'form-control'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Correo electrónico',
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

        def save(self, commit=True):
            user = super().save(commit)
            nombre = self.cleaned_data['nombre']
            apellido = self.cleaned_data['apellido']
            email = self.cleaned_data['email']
            cliente = Cliente(user=user, nombre=nombre, apellido=apellido, email=email)
            if commit:
                cliente.save()
            return user