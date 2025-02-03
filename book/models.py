from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class BookCover(models.Model):
    #The cover image for the booking page
    cover_image = CloudinaryField('image', default='placeholder')
    booking_intro = models.TextField(max_length=200, null=False, blank=False)

    class Meta:
        verbose_name = 'Booking Cover'
        verbose_name_plural = 'Booking Covers'

    def __str__(self):
        #Represent
        return f'Booking introduction'


#Model for barbers
class Barber(models.Model):
    barber_name = models.TextField(max_length=50)
    barber_address = models.CharField(max_length=200)
    barber_number = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']
        
    def __str__(self):
        return f'{self.barber_name}'

#Model for barbers'service
class BarberService(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE, related_name='services')
    service_name = models.TextField(max_length=50)
    service_price = models.DecimalField(max_digits=5, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f'{self.service_name}'


#Booking model to store user inputs, the choice of barber and service
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    service = models.ForeignKey(BarberService, on_delete=models.CASCADE)