from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class BookCover(models.Model):
    #The cover image for the booking page
    cover_image = CloudinaryField('image', default='placeholder')
    booking_intro = models.TextField(max_length=200, null=False, blank=False)

    def __str__(self):
        #Represent
        return self.booking_intro