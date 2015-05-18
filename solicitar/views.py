from django.shortcuts import render,get_object_or_404
from solicitar.models import *
# Create your views here.
def solicitar(request):
	marcas = Marca.objects.all().order_by('orden')
	return render(request, 'solicitar.html' , {"marcas" : marcas})
def modelo(request, marca):
	modelo = Modelo.objects.filter(marca=Marca.objects.get(url=marca)).order_by('orden')
	return render(request, 'modelos.html' , {"modelos" : modelo})
def reparacion(request,marca, modelo):
	reparacion = Reparacion.objects.filter(modelo=Modelo.objects.get(url=modelo)).order_by('orden')
	return render(request, 'reparacion.html' , {"reparaciones" : reparacion})