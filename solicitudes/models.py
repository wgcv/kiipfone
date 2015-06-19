from django.db import models
from solicitar.models import *
from django.contrib.auth.models import User

# Create your models here.

class Solicitud(models.Model):
	id = models.AutoField(primary_key=True)
	fecha_solicitud = models.DateField(auto_now_add=True)
	fecha_modificacion = models.DateField(auto_now=True)
	marca = models.ForeignKey(Marca, blank=True)
	modelo = models.ForeignKey(Modelo, blank=True)
	color = models.ForeignKey(Color, blank=True, null = True)
	reparacion = models.ForeignKey(Reparacion, blank=True)
	pais = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=50)
	telefono = models.CharField(max_length=50)
	observaciones = models.CharField(max_length=1000)
	user = models.OneToOneField(User)
	leido = models.BooleanField(default=False)
	coordinado = models.BooleanField(default=False)
	finalizado = models.BooleanField(default=False)
	def __str__(self):
		return "%s - %s || %s || %s" % (self.modelo, self.marca, self.fecha_solicitud, self.finalizado)
