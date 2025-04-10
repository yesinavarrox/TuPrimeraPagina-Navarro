from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from .models import Producto, Cliente
from .forms import ClienteForm, RegistroForm

# CLIENTES - Login - Registro:

class ClienteView(LoginView):
    template_name = 'blog/login.html'
    authentication_form = ClienteForm
    next_page = reverse_lazy('HoneyPanqui:home')
    
    def form_valid(self, form):
        usuario = form.get_user()
        messages.success(self.request, f"¡{usuario.username}, a comer todos los hotcakes en tu sesión!")
        return super().form_valid(form)

class RegistroView(CreateView):
    form_class = RegistroForm
    template_name = 'blog/registro.html'
    success_url = reverse_lazy('HoneyPanqui:login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "¡Registro Completado. ¡Ahora puedes comprar hotcakes iniciando tu sesión!")
        return super().form_valid(form)

#PEDIDOS


# NAVEGACIÓN:

def inicio(request):
    return render (request, 'blog/index.html')

# READ para productos
def lista_productos(request):
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.all()
    return render(request, 'blog/lista_productos.html', {'productos': productos})

def about(request):
    return render (request, 'blog/about.html')