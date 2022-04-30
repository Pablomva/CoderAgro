from django.db import models


class Contenido(models.Model):
    titulo = models.CharField(max_length=250)
    tema = models.CharField(max_length=250)
    cultivo = models.CharField(max_length=250)
    contenido = models.TextField()
    posteador = models.CharField(max_length=250)
