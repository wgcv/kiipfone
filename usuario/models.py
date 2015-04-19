# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.OneToOneField(User)
	celular = models.CharField("Número de celular", max_length=20)
	nombre = models.CharField("Nombre", max_length=50, blank=True)
	apellido = models.CharField("Apellido", max_length=50, blank=True)
	apellidoMaterno = models.CharField("Apellido materno", max_length=50, blank=True)
	cedula = models.CharField("Cédula", max_length=20, blank=True)
	direccion = models.CharField("Dirección", max_length=150, blank=True)
	def __str__(self):
		return self.user.username
	def email(self):
		return self.user.email