from django import forms
from .models import Booking
from datetime import date, datetime


class DateInput(forms.DateInput):
    """
    Custom date input widget that sets the default value to today's date
    and ensures the correct input type for HTML5 date picker.
    """

    input_type = 'date'

    def __init__(self, *args, **kwargs):
        """
        Initialize the DateInput widget, setting the default 'today' attribute
        to the current date.
        """
        kwargs.setdefault('attrs', {})
        kwargs['attrs']['today'] = date.today().strftime('%Y-%m-%d')
        super().__init__(*args, **kwargs)


class TimeInput(forms.TextInput):
    """
    Custom time input widget that sets the minimum time for selection
    to the current time and ensures the
    correct input type for HTML5 time picker.
    """

    input_type = 'time'

    def __init__(self, *args, **kwargs):
        """
        Initialize the TimeInput widget, setting the 'min' attribute to the
        current time (ensuring the user can't select a time in the past).
        """
        kwargs.setdefault('attrs', {})
        kwargs['attrs']['min'] = datetime.now().strftime('%H:%M')
        super().__init__(*args, **kwargs)


class BookingForm(forms.ModelForm):
    """
    Form for creating or updating a booking, using the Booking model.
    Includes custom widgets for date and time input fields.
    """

    class Meta:
        model = Booking
        fields = ('barber', 'service', 'date', 'time')
        widgets = {
            'date': DateInput(),
            'time': TimeInput(),
        }
