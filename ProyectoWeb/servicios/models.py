from django.db import models

# Create your models here.

class Servicio(models.Model):


    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to="Servicios")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
