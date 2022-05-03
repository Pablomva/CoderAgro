from django.urls import path
from . import views

urlpatterns = [
    path("",views.inicio,name="InicioUsuarios"),
    path("nuevo_productor",views.nuevo_productor,name="NuevoProductor"),
    path("nuevo_asesortecnico", views.nuevo_asesortecnico,name="NuevoAsesorTecnico"),
    path("nuevo_agrocomercio",views.nuevo_agrocomercio,name="NuevoAgroComercio")

]