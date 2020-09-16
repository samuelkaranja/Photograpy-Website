from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="home"),
    path('About/', views.About, name="about"),
    path('Contact-Us/', views.Contact, name="contact"),
]
