from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView
from .models import *

# Create your views here.
class Directorio(ListView):
    model =  DirectorioModel
    template_name = 'azuldirectorio/list.html'