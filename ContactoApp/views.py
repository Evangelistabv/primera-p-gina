from django.shortcuts import render,redirect
from ContactoApp.forms import Formulariocontacto
from django.core.mail import EmailMessage
# Create your views here.
def contacto(request):
	formulario=Formulariocontacto()
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
				email.send()

				return redirect("/contacto/?valido")
			except:
				return redirect("/contacto/?novalido")
	return render(request,"Contacto/contacto.html",{'miformulario':formulario})