class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        
        self.carrito = carrito
    
    def agregar(self, producto):
        if (str(producto.id) not in self.carrito.keys()):
            self.carrito[producto.id] = {
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url,
            }
        else:
            for key, value in self.carrito.items():
                if key==str(producto.id):
                    value["cantidad"] += 1
                    value["precio"] = float(value["precio"])+producto.precio
                    break
        
        self.guardar_carrito()
            #self.carrito[producto.id][cantidad] += 1
        
    def eliminar(self, producto):
        if (str(producto.id) in self.carrito.keys()):
            #print(self.carrito.keys())
            #print(producto.id)
            del self.carrito[str(producto.id)]
            #self.carrito.pop(producto.id)
        self.guardar_carrito()
    
    def restar(self, producto):
        if (str(producto.id) in self.carrito.keys()):
            for key, value in self.carrito.items():
                if key==str(producto.id):
                    value["cantidad"] -= 1
                    value["precio"] = float(value["precio"])-producto.precio
                    if value["cantidad"] < 1: #If cantidad is zero, delete the item
                        self.eliminar(producto)
                    break
        self.guardar_carrito()
    
    def limpiar(self):
        self.carrito = {}
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True