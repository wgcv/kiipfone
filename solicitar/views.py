# -*- encoding: utf-8 -*-
import datetime

from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from usuario.models import *
from solicitudes.models import *
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
		marca = Marca.objects.get(url=marca)
		modelo = Modelo.objects.get(url=modelo)
		reparacion =Reparacion.objects.get(url=reparacion)
		user = request.user
		#falta de implementar color
		solicitud = Solicitud(marca =  marca, modelo = modelo, reparacion = reparacion , pais = request.POST.get('pais'), ciudad = request.POST.get('ciudad'), telefono = request.POST.get('telefono'), observaciones = request.POST.get('observaciones'), user = user)
		solicitud.save()
		return render(request, 'solicitado.html')
	else:
		modelo = Modelo.objects.get(url=modelo)
		reparacion = Reparacion.objects.get(url=reparacion)
		color = modelo.color.all()
		return render(request, 'solicitar.html' , {"modelo":modelo,"reparacion":reparacion,"colores" : color})