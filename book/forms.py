from django import forms
from .models import Booking

#Time and date for the booking
class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TextInput):
    input_type = 'time'

#Create form for the booking model using model form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('barber', 'service', 'date', 'time')
        widgets = {
            'date': DateInput(),
            'time': TimeInput()
        }
        