from django import forms
from .models import Booking, BarberService, Barber

#Create form for the booking model using model form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['barber', 'service']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #populate services based on the selected barber
        if 'barber' in self.data:
            barber_id = self.data.get('barber')
            self.fields['service'].queryset = BarberService.objects.filter(barber_id=barber_id)
        else:
            #Don't show services until user chooses the barber
            self.fields['service'].queryset = BarberService.objects.none()

    def cleaned_data(self):
        service = self.cleaned_data.get('service')
        if not service:
            raise forms.ValidationError('You need to select a service.')
        else:
            return service