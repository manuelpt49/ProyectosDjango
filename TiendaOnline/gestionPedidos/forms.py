from django import forms

class FormularioContacto(forms.Form):
    asunto = forms.CharField(max_length=30)
    email = forms.EmailField()
    mensaje = forms.CharField(max_length=200)