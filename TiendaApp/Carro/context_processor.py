def importe_total_carro(request):
    total = 0
    cantidad = 0
    carro = request.session.get("carro", {})

    for value in carro.values():
        precio = float(value.get("precio", 0))
        unidades = int(value.get("cantidad", 0))
        total += precio * unidades
        cantidad += unidades

    return {
        "importe_total_carro": total,
        "cantidad_total_carro": cantidad,
    }
