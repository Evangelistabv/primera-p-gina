from django.shortcuts import get_object_or_404, redirect, render

from .Carro.carro import Carro
from .models import Producto


def tienda(request):
    productos = Producto.objects.all()
    return render(request, "Tienda/tienda.html", {"productos": productos})


def agregar(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carro.agregar(producto=producto)
    return redirect("tienda")


def eliminar(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("tienda")


def restar(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carro.restar(producto=producto)
    return redirect("tienda")


def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("tienda")
