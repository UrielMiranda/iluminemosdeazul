from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.Contacto.as_view(), name="contactoapp"),
]
