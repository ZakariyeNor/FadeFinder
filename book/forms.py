from django import forms
from .models import Booking
from datetime import date, datetime

#Time and date for the booking
class DateInput(forms.DateInput):
    input_type = 'date'
    attrs = {
        'today': date.today().strftime('%Y-%m-%d'),
    }

class TimeInput(forms.TextInput):
    input_type = 'time'
    attrs = {
        'min': datetime.now().strftime('%H:%M'),
    }

#Create form for the booking model using model form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('barber', 'service', 'date', 'time')
        widgets = {
            'date': DateInput(),
            'time': TimeInput()
        }