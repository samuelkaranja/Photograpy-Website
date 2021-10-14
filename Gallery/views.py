from django.shortcuts import render, redirect
from . models import *
from . forms import ContactForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.

def Index(request):
	image = Gallery.objects.all()
	
	return render(request, 'Gallery/index.html', {'image' : image})

def Image(request, pk):
	spec = Gallery.objects.filter(pk=pk)

	slide = Gallery.objects.all()

	photo = spec | slide

	return render(request, 'Gallery/image.html', {'photo' : photo, 'pk': pk})

def About(request):
	return render(request, 'Gallery/about.html')

def Contact(request):
	form = ContactForm()

	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():
			contact_name = form.cleaned_data['name']
			contact_email = form.cleaned_data['email']
			contact_message = form.cleaned_data['comment']
			
		template = render_to_string('Gallery/email_template.html', {'name': contact_name})

		email = EmailMessage(
			'Thank you',
			template,
			settings.EMAIL_HOST_USER,
			[contact_email]
		)
		
		email.fail_silently=False
		email.send()



		return redirect('home')
		
	return render(request, 'Gallery/contact.html', {'form': form})