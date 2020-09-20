from django.urls import path
from . import views

urlpatterns = [
    path('wedding-photograpy/favourites/', views.Favourites, name="favourite"),
    path('wedding-photograpy/ceremony-reception-venues/', views.Ceremonys, name="ceremony"),
    path('wedding-photograpy/engagements/', views.Engagements, name="engagement"),
    path('Photo/<int:pk>/', views.Image, name='photo'),
]
