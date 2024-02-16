from django.contrib import admin
from BlogApp.models import Categoria,Post
# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
	"""docstring for CategoriaAdmin"""
	readonlyfields=('created','updated')

class PostAdmin(admin.ModelAdmin):
	readonlyfields=('created','updated')
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Post,PostAdmin)