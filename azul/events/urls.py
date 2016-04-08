from django.conf.urls import url
from events.views import *
#from eventbrite import Eventbrite

urlpatterns = [

    url(r'^$', Eventos.as_view(), name='eventos'),
]