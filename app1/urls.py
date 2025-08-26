# pedidos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.listaProyectos.as_view(), name='proyectos'),
    path('inicio/proyecto/<int:pk>/', views.proyectoDetalle, name='proyectoDetalle'),
]
