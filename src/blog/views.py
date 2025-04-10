from django.shortcuts import render

from .models import Producto


# PRODUCTOS:

# NAVEGACIÓN:

def inicio(request):
    return render (request, 'blog/index.html')

def lista_productos(request):
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.all()
    return render(request, 'blog/lista_productos.html', {'productos': productos})

def about(request):
    return render (request, 'blog/about.html')