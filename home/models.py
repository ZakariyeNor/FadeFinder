from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class BarberInfo(models.Model):
    #Model for barber description
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Created by | {self.title}"


#Model for services description
class ServicesDes(models.Model):
    #Services that the barbershop offers
    title = models.CharField(max_length=200)
    services = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title}"