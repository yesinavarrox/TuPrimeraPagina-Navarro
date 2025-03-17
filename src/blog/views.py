from django.shortcuts import render

from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'blog/lista_productos.html', {'productos': productos})
