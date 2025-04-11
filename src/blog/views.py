from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from .models import Producto, Cliente, Pedido
from .forms import ClienteForm, RegistroForm
from decimal import Decimal

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
    success_url = reverse_lazy('HoneyPanqui:home')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "¡Registro Completado. ¡Ahora puedes comprar hotcakes iniciando tu sesión!")
        return super().form_valid(form)

#PEDIDOS

@login_required
def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos_en_carrito = []
    total = 0

    for producto_id, cantidad in carrito.items():
        producto = get_object_or_404(Producto, pk=producto_id)
        subtotal = producto.precio * cantidad
        total += subtotal
        productos_en_carrito.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal,
        })

    return render(request, 'blog/carrito.html', {
        'productos': productos_en_carrito,
        'total': total
    })

@login_required
def agregar_al_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})

    producto_id_str = str(producto_id)
    if producto_id_str in carrito:
        carrito[producto_id_str] += 1
    else:
        carrito[producto_id_str] = 1

    request.session['carrito'] = carrito
    messages.add_message(request, messages.INFO, "Producto agregado al carrito.", extra_tags='carrito')
    return redirect('HoneyPanqui:lista_productos')

@login_required
def confirmar_pedido(request):
    carrito = request.session.get('carrito', {})
    if not carrito:
        return redirect('HoneyPanqui:ver_carrito')

    cliente, creado = Cliente.objects.get_or_create(user=request.user)
    pedido = Pedido(cliente=cliente, total=0)
    pedido.save()

    total = Decimal('0.00')

    for producto_id, cantidad in carrito.items():
        producto = get_object_or_404(Producto, pk=producto_id)
        pedido.productos.add(producto)
        total += producto.precio * cantidad

    pedido.total = total
    pedido.save()

    request.session['carrito'] = {}
    return redirect('HoneyPanqui:ver_pedidos')

@login_required
def ver_pedidos(request):
    cliente = get_object_or_404(Cliente, user=request.user)
    pedidos = Pedido.objects.filter(cliente=cliente).order_by('-id')  
    return render(request, 'blog/pedidos.html', {'pedidos': pedidos})

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