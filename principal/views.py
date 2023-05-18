from django.shortcuts import render




def home(request):
    return render(request, "index.html")
# Create your views here.


# librerias del crud
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#importo el modelo de la base de datos de models.py
from .models import *
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

def Home(request):
    return render(request,"index.html")
def Login(request):
    return render(request,"Login.html")

class Listadomunicipio(ListView):
    model =  Municipio

class municipioCrear(SuccessMessageMixin, CreateView):
    model =Municipio
    form = Municipio
    fields = "__all__"
    success_message ='Municipio creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class municipioDetalle (DetailView):
    model =Municipio

class  municipioActualizar(SuccessMessageMixin,UpdateView):
    model =  Municipio
    form = Municipio
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Municipio Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class municipioEliminar(SuccessMessageMixin, DeleteView): 
    model = Municipio
    form = Municipio
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Municipio Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class Listadotdoc(ListView):
    model = Tdoc
    
    
class tdocCrear(SuccessMessageMixin, CreateView):
    model =Tdoc
    form = Tdoc
    fields = "__all__"
    success_message ='Tdoc creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class tdocDetalle (DetailView):
    model = Tdoc

class  tdocActualizar(SuccessMessageMixin,UpdateView):
    model =  Tdoc
    form = Tdoc
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tdoc Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class tdocEliminar(SuccessMessageMixin, DeleteView): 
    model = Tdoc 
    form = Tdoc
    fields = "__all__"     
 
    # Redireccionamos a la pagina principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tdoc Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'


class Listadoctaller(ListView):
    model =  Ctaller
      
class ctallerCrear(SuccessMessageMixin, CreateView):
    model = Ctaller
    form =  Ctaller
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class ctallerDetalle (DetailView):
    model = Ctaller

class  ctallerActualizar(SuccessMessageMixin,UpdateView):
    model =   Ctaller
    form =  Ctaller
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class ctallerEliminar(SuccessMessageMixin, DeleteView): 
    model =  Ctaller
    form =  Ctaller
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'


class Listadotipersona(ListView):
    model =  Tipersona
    
class tipersonaCrear(SuccessMessageMixin, CreateView):
    model = Tipersona
    form =  Tipersona
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class tipersonaDetalle (DetailView):
    model = Tipersona

class  tipersonaActualizar(SuccessMessageMixin,UpdateView):
    model =   Tipersona
    form =  Tipersona
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class tipersonaEliminar(SuccessMessageMixin, DeleteView): 
    model =  Tipersona 
    form =  Tipersona
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'


class Listadocateserv(ListView):
    model = Cateserv
        
class cateservCrear(SuccessMessageMixin, CreateView):
    model =Cateserv
    form = Cateserv
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class cateservDetalle (DetailView):
    model =Cateserv

class  cateservActualizar(SuccessMessageMixin,UpdateView):
    model =  Cateserv
    form = Cateserv
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class cateservEliminar(SuccessMessageMixin, DeleteView): 
    model = Cateserv 
    form = Cateserv
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
 
        
class Listadoscripcion(ListView):
    model = Scripcion
    
class scripcionCrear(SuccessMessageMixin, CreateView):
    model =Scripcion
    form = Scripcion
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class scripcionDetalle (DetailView):
    model =Scripcion

class  scripcionActualizar(SuccessMessageMixin,UpdateView):
    model =  Scripcion
    form = Scripcion
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class scripcionEliminar(SuccessMessageMixin, DeleteView): 
    model = Scripcion 
    form = Scripcion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
 
class Listadocateserv(ListView):
    model = Cateserv
    
class cateservCrear(SuccessMessageMixin, CreateView):
    model =Cateserv
    form = Cateserv
    fields = "__all__"
    success_message ='Cateserv creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class cateservDetalle (DetailView):
    model =Cateserv

class  cateservActualizar(SuccessMessageMixin,UpdateView):
    model =  Cateserv
    form = Cateserv
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Cateserv Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class cateservEliminar(SuccessMessageMixin, DeleteView): 
    model = Cateserv 
    form = Cateserv
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Cateserv Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
class Listadofactcabeza(ListView):
    model =  Factcabeza

class factcabezaCrear(SuccessMessageMixin, CreateView):
    model =Factcabeza
    form = Factcabeza
    fields = "__all__"
    success_message ='Factcabeza creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class factcabezaDetalle (DetailView):
    model =Factcabeza

class  factcabezaActualizar(SuccessMessageMixin,UpdateView):
    model =  Factcabeza
    form = Factcabeza
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Factcabeza Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class factcabezaEliminar(SuccessMessageMixin, DeleteView): 
    model = Factcabeza
    form = Factcabeza
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Factcabeza Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
class Listadopersona(ListView):
    model =  Persona

class personaCrear(SuccessMessageMixin, CreateView):
    model =Persona
    form = Persona
    fields = "__all__"
    success_message ='Persona creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class personaDetalle (DetailView):
    model =Persona

class  personaActualizar(SuccessMessageMixin,UpdateView):
    model =  Persona
    form = Persona
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Persona Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class personaEliminar(SuccessMessageMixin, DeleteView): 
    model = Persona
    form = Persona
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Persona Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class Listadocuerpo(ListView):
    model = Cuerpo
    
class cuerpoCrear(SuccessMessageMixin, CreateView):
    model =Cuerpo
    form = Cuerpo
    fields = "__all__"
    success_message ='Cuerpo creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class cuerpoDetalle (DetailView):
    model =Cuerpo

class  cuerpoActualizar(SuccessMessageMixin,UpdateView):
    model =  Cuerpo
    form = Cuerpo
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Cuerpo Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class cuerpoEliminar(SuccessMessageMixin, DeleteView): 
    model = Cuerpo 
    form = Cuerpo
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Cuerpo Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
    
class Listadoservicio(ListView):
    model = Servicio
    
class servicioCrear(SuccessMessageMixin, CreateView):
    model =Servicio
    form = Servicio
    fields = "__all__"
    success_message ='Servicio creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class servicioDetalle (DetailView):
    model =Servicio

class  servicioActualizar(SuccessMessageMixin,UpdateView):
    model = Servicio
    form = Servicio
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Servicio Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class servicioEliminar(SuccessMessageMixin, DeleteView): 
    model = Servicio 
    form = Servicio
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Servicio Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

