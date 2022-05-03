from django.contrib import admin
from .models import AsesorTecnico, Productor, AgroComercio

admin.site.register(Productor)
admin.site.register(AsesorTecnico)
admin.site.register(AgroComercio)


