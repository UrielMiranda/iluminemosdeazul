from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^', Artist.as_view(), name='galery'),
]
