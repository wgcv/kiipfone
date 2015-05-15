from django.conf.urls import url
from django.contrib import admin

from solicitar import views

urlpatterns = (
	url(r'^solicitar/$', 'solicitar.views.solicitar', name='solicitar'),
	url(r'^solicitar/(\w+)/$', 'solicitar.views.modelo', name='modelo'),
	url(r'^solicitar/(\w+)/(\w+)/$', 'solicitar.views.reparacion', name='reparacion'),

    )