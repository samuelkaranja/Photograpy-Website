from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request, 'Gallery/index.html')

def Contact(request):
    return render(request, 'Gallery/contact.html')