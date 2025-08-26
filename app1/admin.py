from django.contrib import admin
from .models import Imagen, imagenPublicacion, Publicacion
# Register your models here.
# INLINE DETALLE DE ORDEN ---------------------------->
class ImagenInline(admin.TabularInline):
    model = imagenPublicacion

class OrdenAdmin(admin.ModelAdmin):
    inlines = [
        ImagenInline,
    ]

    
admin.site.register(Publicacion, OrdenAdmin)
admin.site.register(Imagen)