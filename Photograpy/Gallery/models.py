from django.db import models

# Create your models here.

class Gallery(models.Model):
    image = models.ImageField(upload_to="Gallery")
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.name
    