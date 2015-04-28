from django.conf.urls import url
from django.contrib import admin

from sitio import views

urlpatterns = (
	url(r'^$', 'sitio.views.home', name='home'),
	url(r'^base/', 'sitio.views.base', name='base'),
	url(r'^nosotros/', 'sitio.views.nosotros', name='nosotros'),
	url(r'^contactanos/', 'sitio.views.contactanos', name='contactanos'),
    )