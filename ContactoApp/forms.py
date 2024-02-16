from django import forms


class Formulariocontacto(forms.Form):
	nombre=forms.CharField(label="Nombre",required=True)
	email=forms.CharField(label="E-mail",required=True)
	contenido=forms.CharField(label="Contenido",widget=forms.Textarea)
   