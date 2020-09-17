from django.shortcuts import render
from . models import *
# Create your views here.

def Favourites(request):
    fv = Favourite.objects.all()

    return render(request, 'Wedding/favourite.html', {'fv': fv} )

def Ceremonys(request):
    cr = Ceremony.objects.all()

    return render(request, 'Wedding/ceremony.html', {'cr': cr})

def Engagements(request):
    eg = Engagement.objects.all()

    return render(request, 'Wedding/engagements.html', {'eg': eg})