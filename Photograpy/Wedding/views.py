from django.shortcuts import render

# Create your views here.

def Favourite(request):
    return render(request, 'Wedding/favourite.html' )

def Ceremony(request):
    return render(request, 'Wedding/ceremony.html')

def Engagement(request):
    return render(request, 'Wedding/engagements.html')