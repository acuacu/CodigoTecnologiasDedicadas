from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from . import views as core_views


urlpatterns = [
    url(r'^Ingreso/$', auth_views.login, name='login'),
    url(r'^Salir/$', auth_views.logout,{'next_page':'/'}, name='logout'),
    url(r'^$', views.InicioWeb, name='InicioWeb'),
    url(r'^CambiarPpassword/$', views.CambiarPpasswordWeb, name='CambiarPpasswordWeb'),
    url(r'^T9hoib209jWeb/(?P<pk>[0-9]+)/(?P<codigo>[0-9]+)$', views.T9hoib209jWeb, name='T9hoib209jWeb'),
    url(r'^Creando Cuenta/$', views.Crear_cuenta_Web, name='CrearWeb'),
    url(r'^Contactos/$', views.ContactosWeb, name='ContactosWeb'),
    url(r'^Comentarios/$', views.ComentariosWeb, name='ComentariosWeb'),
    url(r'^Soporte/$', views.Soporte, name='ComentariosWeb'),
]
