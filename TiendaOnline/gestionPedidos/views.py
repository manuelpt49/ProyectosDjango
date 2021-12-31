from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from TiendaOnline import settings
from django.core.mail import send_mail
from gestionPedidos.forms import FormularioContacto

# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    data = request.GET['producto']

    if(data):
        if len(data) > 20:
            mensaje="Texto de busqueda demasiado largo"
        else:
        #mensaje = "Buscando... %r" %request.GET['producto']
            articulos = Articulos.objects.filter(nombre__icontains = data)
            return render(request, "resultados_busqueda.html", {'articulos': articulos, 'query': data})
    else:
        mensaje="La búsqueda no tienen datos"
    
    return HttpResponse(mensaje)


def contacto(request):
    if request.method == "POST":
        miformulario = FormularioContacto(request.POST)

        if(miformulario.is_valid()):
            informacion = miformulario.cleaned_data
            #send_mail(informacion['asunto'], informacion['mensaje'], informacion.get('email', ''), ['manuelpt494@gmail.com'],)
            return render(request, "gracias.html", {'informacion': informacion})
            #return HttpResponse(informacion['asunto'], informacion['mensaje'], informacion['email'])
    else:
        miformulario = FormularioContacto() #Constructing a empty form
        return render(request, "formulario_contacto.html", {"formulario": miformulario})
'''

        subject = request.POST["asunto"]
        message = request.POST["mensaje"] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER

        recipient_list = ["manuelpt4940@gmail.com"]

        #send_mail(subject, message, email_from, recipient_list)

        return render(request, "gracias.html")


        return render(request, "gracias.html")
    return render(request, "contacto.html")
'''