from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'kiipfone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls'STATIC_URL = "/static/"
    url(r'^', include('sitio.urls')),

    url(r'^admin/', include(admin.site.urls)),
]