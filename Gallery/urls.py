from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="home"),
    path('portraits/', views.Index, name="portraits"),
    path('portraits/<int:pk>/', views.Image, name="image"),
    path('About/', views.About, name="about"),
    path('Contact-Us/', views.Contact, name="contact"),
]
