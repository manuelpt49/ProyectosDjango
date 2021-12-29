from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.shortcuts import render


def saludo(request): #Primera vista

    #doc_externo = get_template('saludo.html')    
    ctx = {"nombre_persona":"Manuel", "apellido_persona":"Perez", "temas":["plantillas", "Modelo"]} #Data to send to template, always as Dict
    #documento = doc_externo.render(ctx)
    #return HttpResponse(documento)
    return render(request, "saludo.html", ctx)

def curso1(request):
    fecha_actual =datetime.datetime.now()
    return render(request, "Curso1.html", {"fecha":fecha_actual})

def cursoCSS(request):
    fecha_actual =datetime.datetime.now()
    return render(request, "CursoCSS.html", {"nombre":"Manuel"})

def despedida(request):
    return HttpResponse("Adiós") 

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    return HttpResponse(fecha_actual)

def calculaEdad(request, edad, ano):
    periodo = ano - 2021
    edadFutura = edad + periodo
    return HttpResponse("<html><body><h2>En el año %s tendrás %s años </h2></body></html>" %(ano, edadFutura))