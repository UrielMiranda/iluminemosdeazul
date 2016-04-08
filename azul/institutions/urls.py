from django.conf.urls import url
from institutions.views import *
#from eventbrite import Eventbrite

urlpatterns = [

    url(r'^$', AffiliatesView.as_view(), name='afiliados'),
]