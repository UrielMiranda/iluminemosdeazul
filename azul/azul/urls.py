"""azul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from home.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^directorio', include('azuldirectorio.urls')),
    url(r'^galeria', include('galery.urls')),
    url(r'^eventos', include('events.urls')),
    url(r'^posts/', include('posts.urls')),
    url(r'^contacto', include('contacto.urls', namespace='contacto')),
    url(r'^instituciones', include('institutions.urls')),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^donaciones$', TemplateView.as_view(template_name='home/donations.html')),
    url(r'^conocenos$', TemplateView.as_view(template_name='home/conocenos.html')),
    url(r'^a-que-nos-dedicamos', TemplateView.as_view(template_name='home/what-do-we-do.html')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += patterns('',
     (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
