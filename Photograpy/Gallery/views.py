from django.shortcuts import render
from . forms import ContactForm
# Create your views here.

def Index(request):
    return render(request, 'Gallery/index.html')

def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:

        return render(request, 'Gallery/contact.html')