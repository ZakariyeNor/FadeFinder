from django.db import models
from cloudinary.models import CloudinaryField
from book.models import Barber

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=20)
    about_barber = models.ForeignKey(Barber, on_delete=models.CASCADE, related_name='about', null=True, blank=True)
    about_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = ('About Me')
        verbose_name_plural = "About Me"

    def __str__(self):
        barber_name = self.about_barber.barber_name if self.about_barber else "No Barber Assigned"
        return f"{self.title} | {barber_name} | {self.updated_on}"