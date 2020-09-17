from django.urls import path
from . import views

urlpatterns = [
    path('wedding-photograpy/favourites/', views.Favourite, name="favourite"),
    path('wedding-photograpy/ceremony-reception-venues/', views.Ceremony, name="ceremony"),
    path('wedding-photograpy/engagements/', views.Engagement, name="engagement"),
]
