from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import ContactForm
<<<<<<< HEAD

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

# Create your views here.

=======
from django.core.mail import EmailMessage
>>>>>>> 9839424735192f39cbc155b6415e786e54c428e7


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
<<<<<<< HEAD
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
		
=======
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

>>>>>>> 9839424735192f39cbc155b6415e786e54c428e7
		return redirect('contacto:contactoapp')

		
	








	