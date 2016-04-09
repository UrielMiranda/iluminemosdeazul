from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import ContactForm

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

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
			pass

		#Aqui envia email
		plaintext = get_template('contacto/email.txt')
		htmly     = get_template('contacto/email.html')

		d = Context({ 'name': request.POST['nombre_contacto'],
					  'email': request.POST['mail_contacto'],
					  'message': request.POST['contenido'],
					})

		subject, from_email, to = 'Contacto web', 'iluminemosazul@gmail.com', 'fersaavedra85@hotmail.com'
		text_content = plaintext.render(d)
		html_content = htmly.render(d)
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.send()

		return redirect('contacto:contactoapp')





