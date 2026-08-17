from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from ContactoApp.forms import Formulariocontacto


def contacto(request):
    formulario = Formulariocontacto()

    if request.method == "POST":
        formulario = Formulariocontacto(request.POST)

        if formulario.is_valid():
            nombre = formulario.cleaned_data["nombre"]
            correo_usuario = formulario.cleaned_data["email"]
            contenido = formulario.cleaned_data["contenido"]

            mensaje = f"""
Nombre: {nombre}
Correo del usuario: {correo_usuario}

Mensaje:
{contenido}
"""

            send_mail(
                subject=f"Nuevo mensaje de {nombre}",
                message=mensaje,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["TU_CORREO@gmail.com"],
                fail_silently=False,
            )

            return redirect("/contacto/?valido")

    return render(
        request,
        "Contacto/contacto.html",
        {"miformulario": formulario},
    )
