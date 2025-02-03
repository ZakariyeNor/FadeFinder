from django import forms
from .models import Booking, BarberService, Barber

#Create form for the booking model using model form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['barber', 'service']

        