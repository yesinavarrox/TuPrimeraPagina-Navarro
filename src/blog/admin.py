from django.contrib import admin
from . import models

@admin.register(models.Cliente)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "get_username")
    search_fields = ("nombre", "apellido", "user__username")
    ordering = ["apellido"]
    
    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = "Usuario"

@admin.register(models.Producto)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "stock")
    search_fields = ["nombre"]
    ordering = ["nombre"]

@admin.register(models.Pedido)
class PedidosAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha_pedido", "cliente", "total")
    search_fields = ("fecha_pedido", "cliente__nombre")
    ordering = ["cliente"]
    date_hierarchy = ("fecha_pedido")
