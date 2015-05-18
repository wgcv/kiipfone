from django.conf.urls import url
from django.contrib import admin

from solicitar import views

urlpatterns = (
	url(r'^solicitar/$', 'solicitar.views.marca', name='marca'),
	url(r'^solicitar/(\w+)/$', 'solicitar.views.modelo', name='modelo'),
	url(r'^solicitar/(\w+)/(\w+)/$', 'solicitar.views.reparacion', name='reparacion'),
	url(r'^solicitar/(\w+)/(\w+)/(\w+)/$', 'solicitar.views.solicitar', name='solicitar'),

    )