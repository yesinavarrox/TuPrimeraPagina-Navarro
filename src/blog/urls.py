from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import lista_productos
from . import views

app_name = "HoneyPanqui"

urlpatterns = [
# NAVEGACIÓN
    path('', views.inicio, name='home'), 
    path('productos/', lista_productos, name='lista_productos'),
    path('about/', views.about, name="about"),
# CLIENTE
    path('login/', views.ClienteView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('registro/', views.RegistroView.as_view(), name='registro'),
# PRODUCTO
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/confirmar/', views.confirmar_pedido, name='confirmar_pedido'),
    path('pedidos/', views.ver_pedidos, name='ver_pedidos'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]