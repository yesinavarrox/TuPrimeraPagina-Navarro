from django.db import models
from django.contrib.auth.models import User

# Creación de los 3 modelos

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    nacimiento = models.DateField(null=True, blank=True)
    direccion = models.TextField(unique=True)
    
    def __str__(self) -> str:
        return f"{self.user.username} ({self.nombre})"

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.DecimalField(max_digits=20, decimal_places=0)
    
    def __str__(self) -> str:
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    id = models.AutoField(primary_key=True)
    
    def __str__(self) -> str:
        return f"Pedido {self.id} - {self.cliente.user.username}"