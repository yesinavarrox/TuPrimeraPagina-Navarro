from django.shortcuts import render

from .models import Producto

def inicio(request):
    return render (request, 'blog/index.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'blog/lista_productos.html', {'productos': productos})

def about(request):
    return render (request, 'blog/about.html')