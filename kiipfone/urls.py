from django.conf.urls import include, url
from django.contrib import admin
#Borrar al server
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'kiipfone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls'STATIC_URL = "/static/"
    url(r'^', include('sitio.urls')),
    url(r'^', include('usuario.urls')),
    url(r'^', include('solicitar.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #Borrar al server
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)