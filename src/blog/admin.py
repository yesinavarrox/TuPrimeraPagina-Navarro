from django.contrib import admin


from . import models

admin.site.register(models.Cliente)

@admin.register(models.Producto)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "stock")
    search_fields = ["nombre"]
    ordering = ["nombre"]

@admin.register(models.Pedido)
class PedidosAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha_pedido", "cliente", "total")
    search_fields = ("id", "fecha_pedido", "cliente")
    ordering = ["cliente"]
    date_hierarchy = ("fecha_pedido")
