from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from usuario import views


urlpatterns = (
    # Examples:
	url(r'^registrarse/', 'usuario.views.registro', name='registrarse'),
	url(r'^salir/', logout, {'next_page': '/', }, name="salir"),
	url(r'^ingresar/', login, {'template_name': 'ingresar.html', },name="ingresar"),

	#url(r'^ingresar/', login, {'template_name': 'app/template/ingresar.html', }, name="ingresar"),
 	#url(r'^salir/', logout, {'template_name': 'app/template/base.html', }, name="salir"),
    )