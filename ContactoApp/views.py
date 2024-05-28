from django.shortcuts import render,redirect
from ContactoApp.forms import Formulariocontacto
from django.core.mail import EmailMessage,BadHeaderError,send_mail
from .forms import Formulariocontacto
import os
# Create your views here.
def contacto(request):
	formulario=Formulariocontacto()
	emailContacto = os.environ.get('EMAIL_HOST_USER')
	if request.method=='POST':
		formulario=Formulariocontacto(data=request.POST)
		if formulario.is_valid():
			nombre=request.POST.get("nombre")
			email=request.POST.get("email")
			contenido=request.POST.get("contenido")

			email=EmailMessage('Mensaje desde App Django',
				'El usuario {} con direccion {} escribe: \n\n {}'.format(nombre,email,contenido),'',
				['danielluffy10@gmail.com'])
			try:
				send_mail('Mensaje desde App Django',
				'El usuario {} con direccion {} escribe: \n\n {}'.format(nombre,email,contenido),'',
				['danielluffy10@gmail.com'])
			except:
		               return redirect("/contacto/?novalido")
	return render(request,"Contacto/contacto.html",{'miformulario':formulario,'email_contacto':emailContacto})
