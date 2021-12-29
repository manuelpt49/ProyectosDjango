from django.http import HttpResponse
import datetime

def saludo(request): #Primera vista
    return HttpResponse("Hola alumnos")

def despedida(request):
    return HttpResponse("Adiós") 

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    return HttpResponse(fecha_actual)

def calculaEdad(request, edad, ano):
    periodo = ano - 2021
    edadFutura = edad + periodo
    return HttpResponse("<html><body><h2>En el año %s tendrás %s años </h2></body></html>" %(ano, edadFutura))