from django import forms

class ContactForm(forms.Form):
	nombre_contacto= forms.CharField(required=True,label="Dinos tu nombre")
	mail_contacto= forms.EmailField(required=True, label="Pon tu email")
	contenido= forms.CharField(required=True, label="Escribenos tus comentarios", widget=forms.Textarea)
	
	# def __init__(self, *args, **kwargs):
	# 	super(ContactForm, self).__init__(*args, **kwargs)
	# 	self.fields['nombre_contacto'].label = "Dinos tu nombre:"
	# 	self.fields['contact_email'].label = "Pon tu email:"
	# 	self.fields['content'].label = "Escribenos tus comentarios y recibe nuestro boletin"