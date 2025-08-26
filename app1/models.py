from django.db import models

# Create your models here.
# publicaciones/models.py

from django.db import models

class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ManyToManyField("Imagen", through="imagenPublicacion")
    portada = models.ImageField(upload_to='publicaciones/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class imagenPublicacion(models.Model):
    id_imagen = models.ForeignKey("Imagen",on_delete=models.CASCADE)
    id_publicacion = models.ForeignKey("Publicacion",on_delete=models.CASCADE)
    
class Imagen(models.Model):
    imagen = models.ImageField(upload_to='publicaciones/', blank=True, null=True)
    def __str__(self):
        return str(self.id)