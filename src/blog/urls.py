from django.urls import path
from .views import lista_productos
from . import views

app_name = "HoneyPanqui"

urlpatterns = [
# NAVEGACIÓN
    path('', views.inicio, name='home'), 
    path('productos/', lista_productos, name='lista_productos'),
    path('about/', views.about, name="about"),
# PRODUCTO

]