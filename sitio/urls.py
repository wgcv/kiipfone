from django.conf.urls import url
from django.contrib import admin

from sitio import views

urlpatterns = (
	url(r'^$', 'sitio.views.home', name='home'),
    )