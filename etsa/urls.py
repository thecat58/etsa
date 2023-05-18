"""
URL configuration for etsa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LoginView, LogoutView

from re import template

from django.contrib import admin
from django.urls import path
from principal.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',Home,name='index'),
    path('municipio/', Listadomunicipio.as_view(template_name = "municipio/index.html"), name='leer'),
    path('tdoc/', Listadotdoc.as_view(template_name = "tdoc/index.html"), name='leer'),
    
    path('', LoginView.as_view(template_name='login.html'),name='login'),
    
    path('logout/', LoginView.as_view(template_name='login.html'),name='logout'),

    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
path('municipio/detalle/<int:pk>', municipioDetalle.as_view(template_name = "municipio/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('municipio/crear', municipioCrear.as_view(template_name = "municipio/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('municipio/editar/<int:pk>', municipioActualizar.as_view(template_name = "municipio/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('municipio/eliminar/<int:pk>', municipioEliminar.as_view(), name='municipio/eliminar.html'),    

    # La ruta 'tdoc' en donde mostraremos una pagina con los tdoc de un tdoc o registro 
path('tdoc/detalle/<int:pk>', tdocDetalle.as_view(template_name = "tdoc/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo tdoc o registro  
    path('tdoc/crear', tdocCrear.as_view(template_name = "tdoc/crear.html"), name='crear'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('tdoc/editar/<int:pk>', tdocActualizar.as_view(template_name = "tdoc/actualizar.html"), name='actualizar'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un tdoc registro de la Base de Datos 
    path('tdoc/editar/<int:pk>', tdocActualizar.as_view(template_name = "tdoc/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un tdoc o registro de la Base de Datos 
    path('tdoc/eliminar/<int:pk>', tdocEliminar.as_view(), name='tdoc/eliminar.html'),    
 
    
path('ctaller/', Listadoctaller.as_view(template_name = "ctaller/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('ctaller/detalle/<int:pk>', ctallerDetalle.as_view(template_name = "ctaller/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('ctaller/crear', ctallerCrear.as_view(template_name = "ctaller/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('ctaller/editar/<int:pk>', ctallerActualizar.as_view(template_name = "ctaller/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('ctaller/eliminar/<int:pk>', ctallerEliminar.as_view(), name='ctaller/eliminar.html'),    


path('tipersona/', Listadotipersona.as_view(template_name = "tipersona/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('tipersona/detalle/<int:pk>', tipersonaDetalle.as_view(template_name = "tipersona/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('tipersona/crear', tipersonaCrear.as_view(template_name = "tipersona/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('tipersona/editar/<int:pk>', tipersonaActualizar.as_view(template_name = "tipersona/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('tipersona/eliminar/<int:pk>', tipersonaEliminar.as_view(), name='tipersona/eliminar.html'),    


path('cateserv/', Listadocateserv.as_view(template_name = "cateserv/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('cateserv/detalle/<int:pk>', cateservDetalle.as_view(template_name = "cateserv/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('cateserv/crear', cateservCrear.as_view(template_name = "cateserv/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('cateserv/editar/<int:pk>', cateservActualizar.as_view(template_name = "cateserv/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('cateserv/eliminar/<int:pk>', cateservEliminar.as_view(), name='cateserv/eliminar.html'),    


path('scripcion/', Listadoscripcion.as_view(template_name = "scripcion/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('scripcion/detalle/<int:pk>', scripcionDetalle.as_view(template_name = "scripcion/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('scripcion/crear', scripcionCrear.as_view(template_name = "scripcion/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('scripcion/editar/<int:pk>', scripcionActualizar.as_view(template_name = "scripcion/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('scripcion/eliminar/<int:pk>', scripcionEliminar.as_view(), name='scripcion/eliminar.html'),  


path('persona/', Listadopersona.as_view(template_name = "persona/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un persona o registro 
    path('persona/detalle/<int:pk>', personaDetalle.as_view(template_name = "persona/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo persona o registro  
    path('persona/crear', personaCrear.as_view(template_name = "persona/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un persona registro de la Base de Datos 
    path('persona/editar/<int:pk>', personaActualizar.as_view(template_name = "persona/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un persona o registro de la Base de Datos 
    path('persona/eliminar/<int:pk>', personaEliminar.as_view(), name='persona/eliminar.html'),  


path('factcabeza/', Listadofactcabeza.as_view(template_name = "factcabeza/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un factcabeza o registro 
    path('factcabeza/detalle/<int:pk>', factcabezaDetalle.as_view(template_name = "factcabeza/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo factcabeza o registro  
    path('factcabeza/crear', factcabezaCrear.as_view(template_name = "factcabeza/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un factcabeza registro de la Base de Datos 
    path('factcabeza/editar/<int:pk>', factcabezaActualizar.as_view(template_name = "factcabeza/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un factcabeza o registro de la Base de Datos 
    path('factcabeza/eliminar/<int:pk>', factcabezaEliminar.as_view(), name='factcabeza/eliminar.html'),


path('cuerpo/', Listadocuerpo.as_view(template_name = "cuerpo/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un cuerpo o registro 
    path('cuerpo/detalle/<int:pk>', cuerpoDetalle.as_view(template_name = "cuerpo/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo cuerpo o registro  
    path('cuerpo/crear', cuerpoCrear.as_view(template_name = "cuerpo/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un cuerpo registro de la Base de Datos 
    path('cuerpo/editar/<int:pk>', cuerpoActualizar.as_view(template_name = "cuerpo/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un cuerpo o registro de la Base de Datos 
    path('cuerpo/eliminar/<int:pk>', cuerpoEliminar.as_view(), name='cuerpo/eliminar.html'),

path('servicio/', Listadoservicio.as_view(template_name = "servicio/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un servicio o registro 
    path('servicio/detalle/<int:pk>', servicioDetalle.as_view(template_name = "servicio/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo servicio o registro  
    path('servicio/crear', servicioCrear.as_view(template_name = "servicio/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un servicio registro de la Base de Datos 
    path('servicio/editar/<int:pk>', servicioActualizar.as_view(template_name = "servicio/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un servicio o registro de la Base de Datos 
    path('servicio/eliminar/<int:pk>', servicioEliminar.as_view(), name='servicio/eliminar.html'),

]


    





