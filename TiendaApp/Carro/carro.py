class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.carro = self.session.get("carro", {})
        if "carro" not in self.session:
            self.session["carro"] = self.carro

    def agregar(self, producto):
        producto_id = str(producto.id)
        if producto_id not in self.carro:
            self.carro[producto_id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": 1,
                "imagen": producto.imagen.url if producto.imagen else "",
            }
        else:
            self.carro[producto_id]["cantidad"] += 1
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.guardar_carro()

    def restar(self, producto):
        producto_id = str(producto.id)
        if producto_id not in self.carro:
            return
        if self.carro[producto_id]["cantidad"] > 1:
            self.carro[producto_id]["cantidad"] -= 1
        else:
            del self.carro[producto_id]
        self.guardar_carro()

    # Alias para conservar compatibilidad con cualquier llamada antigua.
    def restar_prod(self, producto):
        self.restar(producto)

    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True
        self.carro = self.session["carro"]
