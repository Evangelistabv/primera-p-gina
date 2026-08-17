from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from TiendaApp.Carro.carro import Carro
from TiendaApp.models import Producto


def tienda(request):
    productos = Producto.objects.filter(disponibilidad=True).order_by("id")
    carro = Carro(request)

    return render(
        request,
        "Tienda/tienda.html",
        {
            "productos": productos,
            "carro_items": carro.obtener_items(),
            "importe_total_carro": carro.total(),
            "cantidad_total_carro": carro.total_cantidad(),
        },
    )


def _volver_al_carrito():
    return redirect(f"{reverse('tienda')}#carrito")


def agregar(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id, disponibilidad=True)
    carro.agregar(producto=producto)
    return _volver_al_carrito()


def eliminar(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carro.eliminar(producto=producto)
    return _volver_al_carrito()


def restar(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carro.restar(producto=producto)
    return _volver_al_carrito()


def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return _volver_al_carrito()
