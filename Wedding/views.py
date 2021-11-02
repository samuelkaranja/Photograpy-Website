from django.shortcuts import render
from . models import *
from itertools import chain
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

# def Image(request, pk):
#     fv = Favourite.objects.filter(pk=pk)

#     slide1 = Favourite.objects.all()

#     photo = fv | slide1 

#     return render(request, 'Wedding/image.html', {'photo': photo, 'pk': pk})

def Image(request, pk):
    fv = Favourite.objects.filter(pk=pk)
    slide1 = Favourite.objects.all()

    cr = Ceremony.objects.filter(pk=pk)
    slide2 = Ceremony.objects.all()

    eg = Engagement.objects.filter(pk=pk)
    slide3 = Engagement.objects.all()

    photo1 = fv | slide1

    photo2 = cr | slide2

    photo3 = eg | slide3

    photo = chain(photo1, photo2, photo3)

    return render(request, 'Wedding/image.html', {'photo': photo, 'pk': pk})
