from django.shortcuts import render
from django.http import HttpResponse
from .models import Hilo


def inicio(request):
    return render(request, "usuarios/inicio.html")


def buscar_cultivo(request, cultivo):
    if request.GET.get("titulo"):
        titulo = request.GET.get("titulo")
        hilos = Hilo.objects.filter(titulo__icontains=titulo, cultivo=cultivo)
        return render(request, "paginas/resultado_buscar.html", {"hilos": hilos})

    return render(request, "paginas/buscar.html")


