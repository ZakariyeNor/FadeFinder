from django.db import models
from cloudinary.models import CloudinaryField


#  Create your models here.
#  Model for barber description
class BarberInfo(models.Model):
    """
    Model representing a barber's information including title, description,
    creation date, update date, and an image.
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder')

    # List based on when it created
    class Meta:
        ordering = ['-created_on']

    # String representation of the BarberInfo model.
    def __str__(self):
        return f"Created by | {self.title}"


#  Model for services description
class ServicesDes(models.Model):
    """
    Model representing the services offered by the barbershop, including 
    the title of the service, description, creation date, update date, 
    and an image.
    """

    #  Services that the barbershop offers
    title = models.CharField(max_length=200)
    services = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder')

    # List based on when it created
    class Meta:
        ordering = ['-created_on']

    # String representation of the service model
    def __str__(self):
        return f"{self.title}"
