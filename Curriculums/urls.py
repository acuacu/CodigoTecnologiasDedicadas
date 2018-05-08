from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^Usuario/$', views.Usurio, name='Usuario'),
    url(r'^Curriculum/(?P<pk>[0-9]+)/$', views.CurriculumA, name='Curriculum'),
    url(r'^Curriculum/$', views.CurriculumB, name='Curriculum'),
    url(r'^Curriculum/Eliminar/$', views.CurriculumC, name='Curriculum'),
    url(r'^Curriculum/Crear/$', views.CurriculumD, name='Curriculum'),
]
