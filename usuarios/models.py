from django.db import models

class Productor(models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    email=models.EmailField()
    provincia=models.CharField(max_length=255)
    descripcion=models.TextField()

class Tecnico(models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    email=models.EmailField()
    provincia=models.CharField(max_length=255)
    descripcion=models.TextField()
