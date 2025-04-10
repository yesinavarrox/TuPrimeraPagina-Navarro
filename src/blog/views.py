from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Producto
from .forms import ClienteForm

# CLIENTES:

class ClienteView(LoginView):
    template_name = "blog/login.html"
    authentication_form = ClienteForm
    next_page = reverse_lazy("HoneyPanqui:home")

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