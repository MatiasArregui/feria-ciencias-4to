from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import messages
from .models import Imagen, imagenPublicacion, Publicacion
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.db.models import ProtectedError
from django.views.generic import ListView
import random
import os
# Create your views here.
# PLATO VIEWS ------------------------------------------------------------------------------>
# Listado plato --------------------------->
class listaProyectos(ListView):
    model = Publicacion
    template_name = os.path.join("inicio.html")
    context_object_name = 'publicaciones'
    #Sacamos la paginacion para que nos permita usar los datos presentes en el template
    # paginate_by = 7

def proyectoDetalle(request, pk):
    proyecto = Publicacion.objects.get(id=pk)
    imagenes = [ x.id_imagen for x in imagenPublicacion.objects.all() if x.id_publicacion.id == pk]

    context= {"proyecto" : proyecto, "imagenes" : imagenes}
    return render(request, os.path.join("detalleProyecto.html"), context=context)

        