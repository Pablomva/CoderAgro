from django.shortcuts import render, redirect
from usuarios.models import AgroComercio, AsesorTecnico, Productor
from .forms import FormProductor,FormAsesorTecnico,FormAgroComercio

def inicio(request):
    return render(request, "usuarios/inicio.html")

def nuevo_productor(request):
    if request.method == "POST":
        mi_form = FormProductor(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            produc= Productor(
                nombre=info["nombre"],
                apellido=info["apellido"],
                email=info["email"],
                provincia=info["provincia"],
                descripcion=info["descripcion"],
            )
            produc.save()
            return redirect("InicioUsuarios")

    mi_form = FormProductor()
    return render(request, "usuarios/formProductores.html",{"form": mi_form})

def nuevo_asesortecnico(request):
    if request.method == "POST":
        mi_form = FormAsesorTecnico(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            asetec= AsesorTecnico(
                 nombre=info["nombre"],
                 apellido=info["apellido"],
                 email=info["email"],
                 provincia=info["provincia"],
                 descripcion=info["descripcion"],
                 cultivo=info["cultivo"],
            )
            asetec.save()
            return redirect("InicioUsuarios")

    mi_form = FormAsesorTecnico()
    return render(request, "usuarios/formAsesoresTecnicos.html",{"form": mi_form})

def nuevo_agrocomercio(request):
    if request.method == "POST":
        mi_form = FormAgroComercio(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            agrocom= AgroComercio(
                nombre=info["nombre"],
                razonSocial=info["razonSocial"],
                email=info["email"],
                ubicacion=info["ubicacion"],
                direccion=info["direccion"],
                descripcion=info["descripcion"],
                cultivo=info["cultivo"],
            )
            agrocom.save()
            return redirect("InicioUsuarios")

    mi_form = FormAgroComercio()
    return render(request, "usuarios/formAgroComercio.html",{"form": mi_form})
    