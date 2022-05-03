from django import forms

class FormProductor(forms.Form):
    nombre = forms.CharField(max_length=255)
    apellido = forms.CharField(max_length=255)
    email = forms.EmailField()
    provincia = forms.CharField(max_length=255)
    descripcion = forms.CharField(widget=forms.Textarea)
    cultivo=forms.CharField(max_length=255)

class FormAsesorTecnico(forms.Form):
    nombre=forms.CharField(max_length=255)
    apellido=forms.CharField(max_length=255)
    email=forms.EmailField()
    provincia=forms.CharField(max_length=255)
    descripcion=forms.CharField(widget=forms.Textarea)
    cultivo=forms.CharField(max_length=255)

class FormAgroComercio(forms.Form):
    nombre=forms.CharField(max_length=255)
    razonSocial=forms.CharField(max_length=255)
    email=forms.EmailField()
    ubicacion=forms.CharField(max_length=255)
    direccion=forms.CharField(max_length=255)
    descripcion=forms.CharField(widget=forms.Textarea)
    cultivo=forms.CharField(max_length=255)


