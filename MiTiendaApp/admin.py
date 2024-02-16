from django.contrib import admin
from ServiciosApp.models import Servicio
# Register your models here.
class ServicioAdmin(admin.ModelAdmin):
	"""docstring fos Servicio"""
	readonly_fields=('created','update')
		
admin.site.register(Servicio,ServicioAdmin)