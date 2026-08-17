class Carro:
    SESSION_KEY = "carro"
    TOTAL_KEY = "carro_total_importe"
    COUNT_KEY = "carro_total_cantidad"

    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get(self.SESSION_KEY, {})

        # Django serializa las claves de sesión como texto. Las normalizamos para
        # evitar que un producto aparezca dos veces por usar 1 y "1".
        self.carro = {str(key): value for key, value in carro.items()}
        self._sincronizar_resumen()

    def agregar(self, producto, cantidad=1):
        key = str(producto.id)
        cantidad = max(1, int(cantidad))

        if key not in self.carro:
            imagen = ""
            if getattr(producto, "imagen", None):
                try:
                    imagen = producto.imagen.url
                except ValueError:
                    imagen = ""

            self.carro[key] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": float(producto.precio),
                "cantidad": cantidad,
                "imagen": imagen,
            }
        else:
            self.carro[key]["cantidad"] = int(self.carro[key].get("cantidad", 0)) + cantidad
            self.carro[key]["nombre"] = producto.nombre
            self.carro[key]["precio"] = float(producto.precio)
            if getattr(producto, "imagen", None):
                try:
                    self.carro[key]["imagen"] = producto.imagen.url
                except ValueError:
                    pass

        self.guardar_carro()

    def restar(self, producto):
        key = str(producto.id)
        if key not in self.carro:
            return

        nueva_cantidad = int(self.carro[key].get("cantidad", 1)) - 1
        if nueva_cantidad <= 0:
            del self.carro[key]
        else:
            self.carro[key]["cantidad"] = nueva_cantidad

        self.guardar_carro()

    # Compatibilidad con el nombre anterior del método.
    def restar_prod(self, producto):
        self.restar(producto)

    def eliminar(self, producto):
        key = str(producto.id)
        if key in self.carro:
            del self.carro[key]
            self.guardar_carro()

    def limpiar_carro(self):
        self.carro = {}
        self.guardar_carro()

    def guardar_carro(self):
        self.session[self.SESSION_KEY] = self.carro
        self._sincronizar_resumen()
        self.session.modified = True

    def obtener_items(self):
        items = []
        for item in self.carro.values():
            cantidad = int(item.get("cantidad", 0))
            precio = float(item.get("precio", 0))
            item_render = dict(item)
            item_render["cantidad"] = cantidad
            item_render["precio"] = precio
            item_render["subtotal"] = round(precio * cantidad, 2)
            items.append(item_render)
        return items

    def total(self):
        return round(
            sum(float(item.get("precio", 0)) * int(item.get("cantidad", 0)) for item in self.carro.values()),
            2,
        )

    def total_cantidad(self):
        return sum(int(item.get("cantidad", 0)) for item in self.carro.values())

    def _sincronizar_resumen(self):
        # Guardamos el resumen en sesión para que Base.html pueda mostrarlo en
        # cualquier página sin tocar settings.py ni añadir context processors.
        self.session[self.SESSION_KEY] = self.carro
        self.session[self.TOTAL_KEY] = self.total()
        self.session[self.COUNT_KEY] = self.total_cantidad()
