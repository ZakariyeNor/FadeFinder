from django.db import models
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