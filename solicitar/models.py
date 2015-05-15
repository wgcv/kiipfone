from django.db import models

# Create your models here.

class Marca(models.Model):
	nombre = models.CharField(max_length=50)
	url = models.CharField(max_length=50, unique=True)
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
	url = models.CharField(max_length=50, unique=True)
	descripcion = models.CharField(max_length=150)
	imagen = models.ImageField(upload_to='marcas', blank=False,null=False)
	color = models.ManyToManyField(Color, blank=True)
	marca = models.ForeignKey(Marca)
	def __str__(self):
		return self.nombre

class Reparacion(models.Model):
	nombre = models.CharField(max_length=50)
	url = models.CharField(max_length=50, unique=True)
	descripcion = models.CharField(max_length=800, blank=True)
	costo = models.DecimalField (max_digits=7, decimal_places=2)
	modelo = models.ForeignKey(Modelo)
	tiempo = models.CharField(max_length=50)
	def __str__(self):
		return "%s || %s $%s" % (self.modelo, self.nombre, self.costo)