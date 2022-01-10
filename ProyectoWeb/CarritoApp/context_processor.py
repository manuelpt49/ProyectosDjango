from CarritoApp.carrito import Carrito
def importe_total_carro(request):
    total = 0
    carrito = Carrito(request) #Necessary for creating session
    #if request.user.is_authenticated:
    for key, value in request.session['carrito'].items():
        total += float(value["precio"])
    return {"importe_total_carro":total}