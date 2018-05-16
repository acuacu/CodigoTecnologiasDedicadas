from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from random import randint
from .models import Comentario, Ticket
from django.contrib.auth.models import User
from Curriculums.models import Curriculum as Curri, DatosUsuario as DatosU, ContadorDeCurriculum as Contador
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage
from .forms import AgregarContactosWeb as xxx, AgregarComentariosWeb as com





from django.contrib.auth.models import User
# Create your views here.
def InicioWeb(request):
    #DatosDelUsuario = DatosU.objects.filter(UsuarioDestacado=True)
    destacados = Curri.objects.filter(UsuarioDestacados=True)
    #usuarios = User.objects.all()
    ContadorCurriculum = Contador.objects.filter(pk=1)
    template = loader.get_template('INICIO.html')
    #send_mail("Asunto",
    #         "Mensaje...nLinea 2nLinea3",
    #          '"origen" <walterdaniel.backend@gmail.com>',
    #          ['walterdaniel.backend@gmail.com'])
    context = {
    'destacados' : destacados,
    #'DatosDelUsuario': DatosDelUsuario,
    'ContadorCurriculum' : ContadorCurriculum,
    #'usuarios' : usuarios
    }
    return HttpResponse(template.render(context, request))


def ContactosWeb(request):
    if request.method == 'POST':
        formulario = xxx(request.POST)
        if formulario.is_valid():
            subject = request.POST.get('text_asunto_contacto', None)
            message = request.POST.get('text_texo_del_contacto', None)
            sender = request.POST.get('text_usuario_contacto', None)
            recipients = request.POST.get('text_email_contacto', None)
            email = EmailMessage(subject, message + "Remitente: " +sender, to=[recipients])
            email.send()
            nuevo = formulario.save()
            nuevo.save()
            return HttpResponseRedirect('/')
    else:
        formulario = xxx
    template = loader.get_template('CONTACTO.HTML')
    context = {
        'formulario' : formulario
    }
    return HttpResponse(template.render(context, request))


def ComentariosWeb(request):
    if request.method == 'POST':
        formulario = com(request.POST)
        if formulario.is_valid():
            nuevo = formulario.save()
            nuevo.save()
            return HttpResponseRedirect('/Comentarios')
    else:
        formulario = com
    textos = Comentario.objects.order_by('fecha_de_comentario').reverse()
    template = loader.get_template('COMENTARIOS.HTML')
    context = {
    'textos' : textos, 'formulario' : formulario
    }
    return HttpResponse(template.render(context, request))

















def Soporte(request):
    DatosDelUsuario = Ticket.objects.filter(CuentaDelUsuario=request.user.pk).order_by('FechaDeCreacion')

    template = loader.get_template('SOPORTE.HTML')
    context = {
    'DatosDelUsuario' : DatosDelUsuario
    }
    return HttpResponse(template.render(context, request))








def Crear_cuenta_Web(request):
    if request.method == 'POST':
        accion = request.POST.get('accion', None)
        if accion == 'Registro':
            #Datos del formulario
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            email = request.POST.get('email', None)
            #Datos del Envio de E-mail
            subject = 'Registro exitoso..'
            message = 'Hola '+ username +', la administracion te da la bienvenida a TECNOLOGIAS DEDICADAS.'
            recipients = email
            #Envia E-mail
            emails = EmailMessage(subject,
             message,
              to=[recipients])
            #emails.send()
            #Guarda datos del Usuario
            er = User.objects.create_user(username=username, password=password, email=email)
            er.save()
            return HttpResponseRedirect('/Usuario')
    else:
        template = loader.get_template('REGISTRAR.HTML')
        context = {

        }
        return HttpResponse(template.render(context, request))




def CambiarPpasswordWeb(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        recipients = email
        u = User.objects.get(email=recipients)
        #Datos del Envio de E-mail
        subject = 'CAMBIAR CONTRASEÑA'
        random = str(randint(0,9999999))
        pk = str(u.pk)
        message = 'Hola '+ u.username +', Tu Link: https://www.tecnologiasdedicadas.com/T9hoib209jWeb/'+pk+'/'+random+' .'
        u.set_password(random)
        u.save()
        #Envia E-mail
        emails = EmailMessage(subject,
         message,
          to=[recipients])
        emails.send()
        return HttpResponseRedirect('/')
    else:
        template = loader.get_template('OLVIDO.HTML')
        return HttpResponse(template.render({}, request))




def T9hoib209jWeb(request, pk,codigo):
    u = User.objects.get(pk=pk)
    username = u.username
    if request.method == 'POST':
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if u.check_password(codigo):
            u.set_password(password)
            u.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/Error')
    else:
        context={
        'username' : username
        }
        template = loader.get_template('RECUPERARCONTRASEÑA.HTML')
        return HttpResponse(template.render(context, request))
