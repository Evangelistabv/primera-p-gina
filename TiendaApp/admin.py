from django.contrib import admin
from TiendaApp.models import CategoriaProd,Producto
# Register your models here.
class CategoriaProdAdmin(admin.ModelAdmin):
	"""docstring for CategoriaAdmin"""
	readonlyfields=('created','updated')

class ProductoAdmin(admin.ModelAdmin):
	readonlyfields=('created','updated')
admin.site.register(CategoriaProd,CategoriaProdAdmin)
admin.site.register(Producto,ProductoAdmin)