from django import forms

class formulario(forms.Form):
    nombre = forms.CharField(max_length=10)
    edad = forms.IntegerField()