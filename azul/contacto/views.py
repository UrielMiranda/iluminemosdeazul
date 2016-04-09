from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import ContactForm

from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

# Create your views here.


	# def contact(request):
	# 	form_class = ContactForm

	# 	if request.method == 'POST':
	# 		form = form_class(data=request.POST)
	# 		if form.is_valid():
	# 			nombre_contacto = request.POST.get('nombre_contacto', '')
	# 			mail_contacto = request.POST.get('mail_contacto', '')
	# 			contenido = request.POST.get('contenido', '')

	# 			template= get_template('contact_template.txt')
	# 			context= Context({
	# 				'nombre_contacto': nombre_contacto,
	# 				'mail_contacto': mail_contacto,
	# 				'contenido': contenido,
	# 				})
	# 			content = template.render(context)

	# 			email = EmailMessage("Alquien quiere contactarnos", content,
	# 				"Iluminemos de Azul" + '', ['gaya@iluminemosdeazul.org'],
	# 				headers = {'Reply-to': mail_contacto})
	# 			email.send()
	# 			return redirect('contact')

	# 	return render(request, 'contacto.html', 
	# 		{
	# 		'form': form_class,
	# 		})

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
		email = EmailMessage('Alguien quiere contactarnos', 'contenido template aqui',
			'mail_contacto', ['iluminemosazul@gmail.com'], reply_to= ['madelin.pjm@aoutlook.com'],
			headers={'Mensaje': 'foo'} )

		email.send()
		
		return redirect('contacto:contactoapp')





	