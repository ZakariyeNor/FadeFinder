from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class BookCover(models.Model):
    """
    The cover image for the booking page, along with an introduction text.
    """

    cover_image = CloudinaryField('image', default='placeholder')
    booking_intro = models.TextField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'Booking Cover'
        verbose_name_plural = 'Booking Covers'

    def __str__(self):
        """
        String representation of the BookingCover model.
        """
        return 'Booking introduction'


class Barber(models.Model):
    """
    Model representing a barber, including their name, address, phone number,
    and timestamps for creation and update.
    """

    barber_name = models.CharField(max_length=50)
    barber_address = models.CharField(max_length=200)
    barber_number = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        """
        String representation of the Barber model.
        """
        return self.barber_name


class BarberService(models.Model):
    """
    Model representing the services offered by a barber, including the service
    name, price, and timestamps for creation and update.
    """

    barber = models.ForeignKey(
        Barber, on_delete=models.CASCADE, related_name='services'
    )
    service_name = models.CharField(max_length=50)
    service_price = models.DecimalField(max_digits=5, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        """
        String representation of the BarberService model.
        """
        return self.service_name


class Booking(models.Model):
    """
    Model representing a booking made by a user,
    including the choice of barber,
    service, and the selected time for the appointment.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    service = models.ForeignKey(BarberService, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)

    class Meta:
        ordering = ['-updated_on']
        constraints = [
            models.UniqueConstraint(
                fields=['date', 'time', 'barber'], name='unique_barber_booking'
            )
        ]

    def __str__(self):
        """
        String representation of the Booking model.
        """
        return f"Booked by | {self.user}"
