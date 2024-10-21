from django.shortcuts import render
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




# Create your views here.
