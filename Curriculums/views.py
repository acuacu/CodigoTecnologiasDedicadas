from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from random import randint
from django.contrib.auth.models import User
from .models import Curriculum as CV, Flyers as Fly, Diplomas as Dip, PaginasWeb as PWeb, DatosUsuario as DatosU, ContadorDeCurriculum as contador, DatosUsuario
from .models import FotoDePerfil as FotoDePerfilAS, FotoDelPortada as FotoDePortadaAS
from Web.models import Ticket
from .forms import DatosPersonales as xxx, FotoDePerfilFormulario, FotoDelPortadaFormulario

from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage

# Create your views here.
@login_required
def Usurio(request):
    template = loader.get_template('USUARIO.HTML')
    #send_mail("Asunto",
    #         "Mensaje...nLinea 2nLinea3",
    #          '"origen" <walterdaniel.backend@gmail.com>',
    #          ['walterdaniel.backend@gmail.com'])
    DatosDelUsuario = DatosU.objects.filter(CuentaDelUsuario=request.user.pk)
    curriculum = CV.objects.filter(CuentaDelUsuario=request.user.pk)
    Soporte = Ticket.objects.filter(CuentaDelUsuario=request.user.pk).order_by('FechaDeCreacion')
    #FormImagenes = ImagenesUsuario(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        CuentaDelUsuario = request.user

        if request.POST.get('NuevoUsuario', None) == 'NuevoUsuario':
            ttt = DatosU.objects.create(CuentaDelUsuario=request.user)
            ttt.save()

        if request.POST.get('FotoDePerfil', None) == 'FotoDePerfil':
            FotoDePerfil = request.FILES['FotoDePerfil']
            FotoDePerfilAS.objects.filter(CuentaDelUsuario=CuentaDelUsuario).delete()
            acrualizar = FotoDePerfilAS.objects.filter(CuentaDelUsuario=CuentaDelUsuario).create(CuentaDelUsuario=CuentaDelUsuario, FotoDePerfil=FotoDePerfil)

        if request.POST.get('FotoDePortada', None) == 'FotoDePortada':
            FotoDePortada = request.FILES['FotoDePortada']
            FotoDePortadaAS.objects.filter(CuentaDelUsuario=CuentaDelUsuario).delete()
            acrualizar = FotoDePortadaAS.objects.filter(CuentaDelUsuario=CuentaDelUsuario).create(CuentaDelUsuario=CuentaDelUsuario, FotoDePortada=FotoDePortada)

        if request.POST.get('EditarDatosPersonales', None) == 'EditarDatosPersonales':
            FotoDePortada = request.FILES['FotoDePortada']
            NumeroDeTelefono = request.POST.get('NumeroDeTelefono', None)
            DeQueTrabajo = request.POST.get('DeQueTrabajo', None)
            SegundoFactorDeAutentificacion = request.POST.get('SegundoFactorDeAutentificacion', None)
            print (SegundoFactorDeAutentificacion)
            if SegundoFactorDeAutentificacion == 'on':
                Elemento = True
            else:
                Elemento = False
            DatosUsuario.objects.filter(CuentaDelUsuario=CuentaDelUsuario).delete()
            acrualizar = DatosUsuario.objects.filter(CuentaDelUsuario=CuentaDelUsuario).update(
            CuentaDelUsuario=CuentaDelUsuario,
            NumeroDeTelefono=NumeroDeTelefono,
            DeQueTrabajo=DeQueTrabajo,
            SegundoFactorDeAutentificacion=Elemento)
            #acrualizar.save()
            return HttpResponseRedirect('/Usuario')
        if request.POST.get('CambiarContraseña', None) == 'CambiarContraseña':
            passwordAntiguo = request.POST.get('passwordAntiguo', None)
            passwordNuevo = request.POST.get('passwordNuevo', None)

            u = User.objects.get(pk=request.user.pk)

            if u.check_password(passwordAntiguo):
                u.set_password(passwordNuevo)
                u.save()
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/Error')





    context = {
    'DatosDelUsuario' : DatosDelUsuario,
    'curriculum' : curriculum,
    'Soporte' : Soporte,
    }
    return HttpResponse(template.render(context, request))

def CurriculumA(request, pk):
    template = loader.get_template('CURRICULUM.HTML')
    usuarios = User.objects.filter(pk=pk)
    DatosDelUsuario = DatosU.objects.filter(CuentaDelUsuario=User.objects.filter(pk=pk))
    note='seccion de los CV (usuarios=El usuario dueño de la cuenta.)'
    curriculum = CV.objects.filter(CuentaDelUsuario=User.objects.filter(pk=pk))
    Flyer = Fly.objects.filter(CuentaDelUsuario=User.objects.filter(pk=pk))
    Diploma = Dip.objects.filter(CuentaDelUsuario=User.objects.filter(pk=pk))
    Web = PWeb.objects.filter(CuentaDelUsuario=User.objects.filter(pk=pk))
    #send_mail("Asunto",
    #         "Mensaje...nLinea 2nLinea3",
    #          '"origen" <walterdaniel.backend@gmail.com>',
    #          ['walterdaniel.backend@gmail.com'])
    context = {
    'curriculum' : curriculum,
    'Flyer' : Flyer,
    'Diploma' : Diploma,
    'Web' : Web,
    'DatosDelUsuario' : DatosDelUsuario
     }
    return HttpResponse(template.render(context, request))
@login_required
def CurriculumB(request):
    template = loader.get_template('CREADOR_DE_CURRICULUMS.HTML')
    #usuarios = User.objects.filter(pk=request.user.pk)
    curriculum = CV.objects.filter(CuentaDelUsuario=request.user.pk)
    Flyer = Fly.objects.filter(CuentaDelUsuario=request.user.pk)
    Diploma = Dip.objects.filter(CuentaDelUsuario=request.user.pk)
    Web = PWeb.objects.filter(CuentaDelUsuario=request.user.pk)
    formulario = xxx(request.POST)
    if request.method == 'POST':
        if request.POST.get('NuevoCV', None) == 'NuevoCV':

            actualizar = contador.objects.filter(pk = 1)
            numero = (actualizar[0].contadorCurriculum) + 1
            actualizar = contador.objects.filter(pk = 1).update(contadorCurriculum=numero)
            print(actualizar)
            ttt = CV.objects.create(CuentaDelUsuario=request.user, pkUsuario=request.user.pk)
            ttt.save()
        if request.POST.get('Nuevo_flyer', None) == 'Nuevo_flyer':
            link = request.POST.get('Flyer', None)
            ttt = Fly.objects.create(CuentaDelUsuario=request.user, link=link)
            ttt.save()

        if request.POST.get('Nuevo_Diploma', None) == 'Nuevo_Diploma':
            link = request.POST.get('Diploma', None)
            ttt = Dip.objects.create(CuentaDelUsuario=request.user, link=link)
            ttt.save()
        if request.POST.get('Eliminar_Diploma', None) == 'Eliminar_Diploma':
            pk = request.POST.get('pk', None)
            ttt = Dip.objects.filter(CuentaDelUsuario=request.user, id=pk).delete()


        if request.POST.get('Nuevo_Web', None) == 'Nuevo_Web':
            link = request.POST.get('Web', None)
            ttt = PWeb.objects.create(CuentaDelUsuario=request.user, link=link)
            ttt.save()
        if request.POST.get('Eliminar_Web', None) == 'Eliminar_Web':
            pk = request.POST.get('pk', None)
            ttt = PWeb.objects.filter(CuentaDelUsuario=request.user, id=pk).delete()



        if request.POST.get('Eliminar_flyer', None) == 'Eliminar_flyer':
            pk = request.POST.get('pk', None)
            ttt = Fly.objects.filter(CuentaDelUsuario=request.user, id=pk).delete()

        accion = request.POST.get('Curriculum', None)
        if accion == 'Curriculum':
            Nombre = request.POST.get('Nombre', None)
            Direccion = request.POST.get('Direccion', None)
            Pais = request.POST.get('Pais', None)
            Nacimiento = request.POST.get('Nacimiento', None)
            Edad = request.POST.get('Edad', None)
            Dni = request.POST.get('Dni', None)
            Email = request.POST.get('Email', None)
            Telefono = request.POST.get('Telefono', None)

            EducacionPrimaria = request.POST.get('EducacionPrimaria', None)
            EducacionSecundaria = request.POST.get('EducacionSecundaria', None)
            EducacionOtro = request.POST.get('EducacionOtro', None)
            IdiomaNativo = request.POST.get('IdiomaNativo', None)
            IdiomaSecundario = request.POST.get('IdiomaSecundario', None)
            IdiomaTerciario = request.POST.get('IdiomaTerciario', None)
            EducacionDeImportancia = request.POST.get('EducacionDeImportancia', None)
            OtrosConocimientos = request.POST.get('OtrosConocimientos', None)
            Informatica = request.POST.get('Informatica', None)
            ExperienciaLaboral = request.POST.get('ExperienciaLaboral', None)
            EspectativaDePuesto = request.POST.get('EspectativaDePuesto', None)
            acrualizar = CV.objects.filter(CuentaDelUsuario=request.user).update(Nombre =Nombre,
            Direccion =Direccion,
            Pais =Pais,
            Nacimiento =Nacimiento,
            Edad =Edad,
            Dni =Dni,
            Email =Email,
            Telefono =Telefono,
            EducacionPrimaria =EducacionPrimaria,
            EducacionSecundaria =EducacionSecundaria,
            EducacionOtro =EducacionOtro,
            IdiomaNativo =IdiomaNativo,
            IdiomaSecundario =IdiomaSecundario,
            IdiomaTerciario =IdiomaTerciario,
            EducacionDeImportancia =EducacionDeImportancia,
            OtrosConocimientos =OtrosConocimientos,
            Informatica =Informatica,
            ExperienciaLaboral =ExperienciaLaboral,
            EspectativaDePuesto =EspectativaDePuesto
            )

    context = {
    'curriculum' : curriculum,
    'Flyer' : Flyer,
    'Diploma' : Diploma,
    'Web' : Web
     }
    return HttpResponse(template.render(context, request))

def CurriculumC(request):
    actualizar = contador.objects.filter(pk = 1)
    numero = (actualizar[0].contadorCurriculum) - 1
    actualizar = contador.objects.filter(pk = 1).update(contadorCurriculum=numero)
    curriculum = CV.objects.filter(CuentaDelUsuario=request.user.pk).delete()
    print('numero actual de curiculums {}'.format(actualizar))
    return HttpResponseRedirect('/Usuario')
def CurriculumD(request):
    actualizar = contador.objects.filter(pk = 1)
    numero = (actualizar[0].contadorCurriculum) + 1
    actualizar = contador.objects.filter(pk = 1).update(contadorCurriculum=numero)
    curriculum = CV.objects.create(CuentaDelUsuario=request.user, pkUsuario=request.user.pk)
    print('numero actual de curiculums {}'.format(actualizar))
    return HttpResponseRedirect('/Usuario')

def ContactosWeb(request):
    if request.method == 'POST':
        formulario = xxx(request.POST)
        if formulario.is_valid():
            subject = request.POST.get('text_asunto_contacto', None)
            message = request.POST.get('text_texo_del_contacto', None)
            sender = request.POST.get('text_usuario_contacto', None)
            recipients = request.POST.get('text_email_contacto', None)
            email = EmailMessage(subject, message + "<br> Remitente: " +sender, to=[recipients])
            email.send()
            nuevo = formulario.save()
            nuevo.save()
            return HttpResponseRedirect('/Inicio')
    else:
        formulario = xxx
    template = loader.get_template('CONTACTO.HTML')
    context = {
        'formulario' : formulario
    }
    return HttpResponse(template.render(context, request))
