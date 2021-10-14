from django.db import models

# Create your models here.

class Favourite(models.Model):
    image = models.ImageField(upload_to="Wedding/Favourite")

class Ceremony(models.Model):
    image = models.ImageField(upload_to="Wedding/Ceremony")

class Engagement(models.Model):
    image = models.ImageField(upload_to="Wedding/Engagement")