# -*- encoding: utf-8 -*-
import datetime

from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from usuario.models import *

from solicitar.models import *
# Create your views here.
def marca(request):
	marcas = Marca.objects.all().order_by('orden')
	return render(request, 'marcas.html' , {"marcas" : marcas})
def modelo(request, marca):
	modelo = Modelo.objects.filter(marca=Marca.objects.get(url=marca)).order_by('orden')
	return render(request, 'modelos.html' , {"modelos" : modelo})
def reparacion(request,marca, modelo):
	reparacion = Reparacion.objects.filter(modelo=Modelo.objects.get(url=modelo)).order_by('orden')
	return render(request, 'reparacion.html' , {"reparaciones" : reparacion})
@login_required()
def solicitar(request,marca, modelo,reparacion):
	if request.method == 'POST':
		usuario=Usuario.objects.get(user=request.user)
		reparacion =Reparacion.objects.get(url=reparacion)
		now = datetime.datetime.now()
		send_mail('Reparacion %s || %s' %(request.user.username ,now.strftime("%Y-%m-%d %H:%M")), '', 'kiipfone@gmail.com', ['kiipfone@gmail.com'], html_message='<h1>Informacion del telefono</h1>Marca: %s<br>Modelo: %s<br>Reparacion: %s<br><h1>Informacion Personal</h1>Nombre: %s <br>Apellido: %s<h1>Contacto</h1> Direccion: %s<br> Ciudad: %s<br>Pais: %s<br>Telefono: %s <br>Telefono adicional: %s<br>E-Mail: %s<h1>Informacion adicional: </h1> %s' %(marca,modelo,reparacion.nombre,request.user.first_name,request.user.last_name,request.POST.get('direccion'),request.POST.get('ciudad'),request.POST.get('pais'),usuario.celular,request.POST.get('telefono'),request.user.email,request.POST.get('observaciones')))
		return render(request, 'solicitado.html')
	else:
		modelo = Modelo.objects.get(url=modelo)
		reparacion = Reparacion.objects.get(url=reparacion)
		color = modelo.color.all()
		return render(request, 'solicitar.html' , {"modelo":modelo,"reparacion":reparacion,"colores" : color})