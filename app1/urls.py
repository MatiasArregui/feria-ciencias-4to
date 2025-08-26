# pedidos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaProyectos.as_view(), name='proyectos'),
    path('proyecto/<int:pk>/', views.proyectoDetalle, name='proyectoDetalle'),
]
