from django.shortcuts import render,redirect
from TiendaApp.models import Producto
from TiendaApp.Carro.carro import Carro
# Create your views here.
def tienda(request):
	productos=Producto.objects.all()
	return render(request,"tienda/tienda.html",{"productos":productos})

def agregar(request,producto_id):
	carro=Carro(request)
	producto=Producto.objects.get(id=producto_id)
	carro.agregar(producto=producto)
	return redirect("tienda")

def eliminar(request,producto_id):
	carro=Carro(request)
	producto=Producto.objects.get(id=producto_id)
	carro.eliminar(producto=producto)
	return redirect("tienda")

def restar(request,producto_id):
	carro=Carro(request)
	producto=Producto.objects.get(id=producto_id)
	carro.restar(producto=producto)
	return redirect("tienda")

def limpiar_carro(request,producto_id):
	carro=Carro(request)
	carro.limpiar_carro()
	return redirect("tienda")
