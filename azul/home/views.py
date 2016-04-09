from django.shortcuts import render
from django.views.generic import TemplateView
from posts.models import *

class HomeView(TemplateView):
	template_name= "home/home.html"

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['news'] = Post.objects.latest('publicado')
		context['date'] =  context['news'].fecha.date().isoformat()
		return context

class DonationsView(TemplateView):
	template_name = "home/donations.html"