from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="InicioPags"),
    path("buscar/<cultivo>", views.buscar_cultivo, name="BuscarHilo"),
]