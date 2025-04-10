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
# PRODUCTO
    path('login/', views.ClienteView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout')
]