from django.forms.forms import Form
from django.shortcuts import redirect, render
from BlogApp.models import Categoria
from ContactoApp.forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    if request.method == "POST":
        formulario_contacto = FormularioContacto(data = request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            """Way to send email and manage try catch when the send has troubles"""
            #email = EmailMessage('Mensaje desde App Django',
            #"El usuario {} con la dirección {} escribió lo siguiente: \n\n {}".format(nombre, email, contenido),
            #"", ["manuelpt4940@gmail.com"], reply_to=[email])

            #try:
                #email.send()
            return redirect("/contacto/?valido")
            #except:
            #    return return redirect("/contacto/?invalido")
    else:        
        formulario = FormularioContacto()
        return render(request, 'contacto.html', {'formulario': formulario})
