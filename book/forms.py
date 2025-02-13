from django import forms
from .models import Booking
from datetime import date, datetime

#Time and date for the booking
class DateInput(forms.DateInput):
    input_type = 'date'
    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {})
        kwargs['attrs']['today'] = date.today().strftime('%Y-%m-%d')
        super().__init__(*args, **kwargs)

class TimeInput(forms.TextInput):
    input_type = 'time'
    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {})
        kwargs['attrs']['min'] = datetime.now().strftime('%H:%M')
        super().__init__(*args, **kwargs)

#Create form for the booking model using model form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('barber', 'service', 'date', 'time')
        widgets = {
            'date': DateInput(),
            'time': TimeInput()
        }


