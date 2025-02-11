from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from book.models import Barber

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=20)
    about_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = ('About Me')
        verbose_name_plural = "About Me"

    def __str__(self):
        return f"{self.title} | {self.updated_on}"

#Collaboration form
class Collaboration(models.Model):
    barber_name = models.CharField(max_length=50)
    barber_shop = models.CharField(unique=True, max_length=50)
    business_type = models.CharField(
        choices=[('barber', 'Barber'), ('hair_stylist', 'Hair Stylist'), ('beauty_salon', 'Beauty Salon')],
        max_length=50)
    service_offered = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    more_info = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        constraints = [
            models.UniqueConstraint(fields=['barber_name', 'barber_shop'], name='unique_barber_and_shop')
        ]

    def __str__(self):
        return f"The {self.barber_shop} owned by | {self.barber_name}"


#Contact us form
class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()
    is_finished = models.BooleanField(default=False, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
        constraints = [
            models.UniqueConstraint(fields=['email', 'message'], name='unique_email_and_message')
        ]
        verbose_name = ('User Message')
        verbose_name_plural = ("User Messages")

    def __str__(self):
        return f"Message from {self.name} | {self.created_on}"
