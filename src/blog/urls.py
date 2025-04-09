from django.urls import path
from .views import lista_productos

app_name = "HoneyPanqui"

urlpatterns = [
    path('', lista_productos, name='lista_productos'),
]