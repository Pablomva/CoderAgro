from django.db import models


class Hilo(models.Model):
    titulo = models.CharField(max_length=255)
    tema = models.CharField(max_length=255)
    cultivo=models.CharField(max_length=255)
    posteador = models.CharField(max_length=255)

    def __str__(self):
        return f"[{self.tema}] {self.titulo}"
