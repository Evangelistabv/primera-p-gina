from django.shortcuts import render, redirect
from ContactoApp.forms import Formulariocontacto
from django.core.mail import EmailMessage
from smtplib import SMTPException
from .forms import Formulariocontacto

def contacto(request):
    formulario = Formulariocontacto()
    
    if request.method == 'POST':
        formulario = Formulariocontacto(data=request.POST)
        
        if formulario.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email_message = EmailMessage(
                'Mensaje desde App Django',
                'El usuario {} con dirección {} escribe: \n\n {}'.format(nombre, email, contenido),
                '',
                ['danielluffy10@gmail.com']
            )

            try:
                email_message.send()
                return redirect("/contacto/?valido")
            except SMTPException as e:
                # Captura el error y guárdalo en el contexto para pasarlo a la plantilla
                error_message = str(e)
                return render(request, "Contacto/contacto.html", {'miformulario': formulario, 'error_message': error_message})

    return render(request, "Contacto/contacto.html", {'miformulario': formulario})
