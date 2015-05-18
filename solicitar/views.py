from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from solicitar.models import *
# Create your views here.
def marca(request):
	marcas = Marca.objects.all().order_by('orden')
	return render(request, 'solicitar.html' , {"marcas" : marcas})
def modelo(request, marca):
	modelo = Modelo.objects.filter(marca=Marca.objects.get(url=marca)).order_by('orden')
	return render(request, 'modelos.html' , {"modelos" : modelo})
def reparacion(request,marca, modelo):
	reparacion = Reparacion.objects.filter(modelo=Modelo.objects.get(url=modelo)).order_by('orden')
	return render(request, 'reparacion.html' , {"reparaciones" : reparacion})
@login_required()
def solicitar(request,marca, modelo,reparacion):
	send_mail('Reparacion', '', 'kiipfone@gmail.com', ['gstavocevallos@gmail.com'], html_message='Marca: %s<br>Modelo: %s<br>Reparacion: %s' %(marca,modelo,reparacion))
	marcas = Marca.objects.all().order_by('orden')
	return render(request, 'solicitar.html' , {"marcas" : marcas})