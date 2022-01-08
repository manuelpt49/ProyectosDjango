from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(max_length=20, label="Nombre", required=True)
    email = forms.EmailField(label="Email")
    contenido = forms.CharField(max_length=500, label="Contenido", widget=forms.Textarea)