from django.db import models

# Create your models here.

class Marca(models.Model):
	nombre = models.CharField(max_length=50)
	imagen = models.ImageField(upload_to='marcas', blank=False,null=False)
	def __str__(self):
		return self.nombre

class Color(models.Model):
	nombre = models.CharField(max_length=50)
	codigo = models.CharField(max_length=10)
	def __str__(self):
		return "%s || %s" % (self.nombre, self.codigo)

class Modelo(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=150)
	imagen = models.ImageField(upload_to='marcas', blank=False,null=False)
	color = models.ForeignKey(Color, blank=True,null=True)
	marca = models.OneToOneField(Marca)

	def __str__(self):
		return self.nombre

class Reparacion(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=800, blank=True)
	costo = models.DecimalField (max_digits=7, decimal_places=2)
	modelo = models.OneToOneField(Modelo)
	tiempo = models.CharField(max_length=50)
	def __str__(self):
		return "%s $ %s || %s" % (self.modelo, self.costo, self.nombre)