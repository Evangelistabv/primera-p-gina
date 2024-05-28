from django.shortcuts import render, redirect
from ContactoApp.forms import Formulariocontacto
from django.core.mail import EmailMessage, send_mail

def contacto(request):
    formulario = Formulariocontacto()
    if request.method == 'POST':
        formulario = Formulariocontacto(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage('Mensaje desde App Django',
                                 'El usuario {} con dirección {} escribe: \n\n {}'.format(nombre, email, contenido),
                                 '',
                                 ['danielluffy10@gmail.com'])
            try:
                send_mail('Mensaje desde App Django',
                          'El usuario {} con direccion {} escribe: \n\n {}'.format(nombre, email, contenido),
                          '',
                          ['danielluffy10@gmail.com'])
            except Exception as e:
                error = str(e)
                return redirect("/contacto/?error={}".format(error))
    return render(request, "Contacto/contacto.html", {'miformulario': formulario})

