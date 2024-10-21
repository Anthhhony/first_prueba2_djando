from django.shortcuts import render,redirect
from eva2app.models import DBproyecto
from . import forms

def registros(request):
    registro = DBproyecto.objects.all()
    data = {'registro':registro}
    return render(request, "templatesApp/index.html", data)

def agregar(request):
    form = forms.formulario()
    if request.method == "POST":
        form = forms.formulario(request.POST)
        if form.is_valid():
            db = DBproyecto(
                nombre = form.cleaned_data["nombre"],
                edad = form.cleaned_data["edad"]
            )
        db.save()
    data = {"form":form}
    return render(request,"templatesApp/agregar.html", data)

def eliminar(request, idf):
    proyecto = DBproyecto.objects.get(id = idf)
    proyecto.delete()
    return redirect("/")


def actualizar(request, idf):
    project = DBproyecto.objects.get(id = idf)
    form = forms.formulario(instance = project)
    if request.method == "POST":
        form = forms.formulario(request.POST, instance=project)
        if form.is_valid():
            form.save()
        return registros(request)
    data = {"form":form}
    return render(request, "templateApp/agregar.html", data)





# Create your views here.
