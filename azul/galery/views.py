from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView
from .models import *

# Create your views here.
class Artist(ListView):
    model =  ArtistModel
    template_name = 'galery/list.html'