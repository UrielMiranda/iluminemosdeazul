from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView
from .models import *

# Create your views here.
class AffiliatesView(ListView):
    model = Affiliates
    template_name = 'affiliates/list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AffiliatesView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['foundations'] = Affiliates.objects.filter(category=1)
        context['contributors'] = Affiliates.objects.filter(category=2)
        context['vowels'] = Affiliates.objects.filter(category=3)
        return context