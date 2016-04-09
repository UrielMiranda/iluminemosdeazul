from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.



class Contacto(View):
	def get(self,request):
		form=ContactForm()
		return render(request, 'contacto/contacto.html',
			{
			'form': form,
			})
	def post(self,request):
		form=ContactForm(request.POST)
		if form.is_valid():

			nombre_contacto= form.cleaned_data['nombre_contacto']
			mail_contacto= form.cleaned_data['mail_contacto']
			contenido= form.cleaned_data['contenido']
		content= """
		Hay alguien interesado en Iluminemos de Azul

		Nombre: %s
		Mail:  %s
		Mensaje: %s"""	% (nombre_contacto, mail_contacto, contenido)
		email = EmailMessage('Alguien quiere contactarnos', content,
			mail_contacto, ['iluminemosazul@gmail.com'], reply_to= [mail_contacto],
			headers={'Mensaje': 'foo'} )
		try:
			email.send()
			print('Exito')
		except:
			print('Error')


		return redirect('contacto:contactoapp')











