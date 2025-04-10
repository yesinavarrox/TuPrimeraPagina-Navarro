from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
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
        fields = ["username", "password1", "password2", "email"]

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
        user = super().save(commit=commit)
        if commit:
            Cliente.objects.create(
                user=user,
                nombre=self.cleaned_data["nombre"],
                apellido=self.cleaned_data["apellido"],
                email=self.cleaned_data["email"],
                nacimiento=self.cleaned_data["nacimiento"],
                direccion=self.cleaned_data["direccion"]
            )
        return user