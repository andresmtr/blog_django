from django.conf.urls import url 
from .views import Inicio, Listado, DetallePost, FormularioContacto
from base import views
from django.urls import path

urlpatterns = [
    path('',Inicio.as_view(), name = 'index'),
    path('Ordenadores/',Listado.as_view(),{'nombre_categoria':'Ordenadores'}, name = 'Ordenadores'),
    path('Videojuegos/',Listado.as_view(),{'nombre_categoria':'Videojuegos'}, name = 'Videojuegos'),
    path('Programación/',Listado.as_view(),{'nombre_categoria':'Programación'}, name = 'Programación'),
    path('Apple/',Listado.as_view(),{'nombre_categoria':'Apple'}, name = 'Apple'),
    path('Google/',Listado.as_view(),{'nombre_categoria':'Google'}, name = 'Google'),
    path('Microsoft/',Listado.as_view(),{'nombre_categoria':'Microsoft'}, name = 'Microsoft'),
    path('Tutoriales/',Listado.as_view(),{'nombre_categoria':'Tutoriales'}, name = 'Tutoriales'),
    path('Tecnología/',Listado.as_view(),{'nombre_categoria':'Tecnología'}, name = 'Tecnología'),
    path('formulario_contacto/', FormularioContacto.as_view(), name = 'formulario_contacto'),
    path('<slug:slug>/',DetallePost.as_view(), name = 'detalle_post'),

    

    # path('<slug:slug>/Ordenadores/',DetallePost.as_view(),{'nombre_categoria':'Ordenadores'}, name = 'Ordenadores'),
    # path('<slug:slug>/Videojuegos/',DetallePost.as_view(),{'nombre_categoria':'Videojuegos'}, name = 'Videojuegos'),
    # path('<slug:slug>/Programación/',DetallePost.as_view(),{'nombre_categoria':'Programación'}, name = 'Programación'),
    # path('<slug:slug>/Apple/',DetallePost.as_view(),{'nombre_categoria':'Apple'}, name = 'Apple'),
    # path('<slug:slug>/Google/',DetallePost.as_view(),{'nombre_categoria':'Google'}, name = 'Google'),
    # path('<slug:slug>/Microsoft/',DetallePost.as_view(),{'nombre_categoria':'Microsoft'}, name = 'Microsoft'),
    # path('<slug:slug>/Tutoriales/',DetallePost.as_view(),{'nombre_categoria':'Tutoriales'}, name = 'Tutoriales'),
    # path('<slug:slug>/Tecnología/',DetallePost.as_view(),{'nombre_categoria':'Tecnología'}, name = 'Tecnología'),
    

]