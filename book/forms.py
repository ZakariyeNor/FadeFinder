from django import forms
from .models import Booking, BarberService, Barber

#Create form for the booking model using model form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('barber', 'service')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



        #Don't show services until user chooses the barber
        self.fields['service'].queryset = BarberService.objects.none()

        #populate services based on the selected barber
        if 'barber' in self.data:
            try:
                barber_id = int(self.data.get('barber'))
                self.fields['service'].queryset = BarberService.objects.filter(barber_id=barber_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            #Don't show services until user chooses the barber
            self.fields['service'].queryset = BarberService.objects.filter(barber=self.instance.barber)

    def clean(self):
        cleaned_data = super().clean()
        service = self.cleaned_data.get('service')
        if not service:
            raise forms.ValidationError('You need to select a service.')
        else:
            return cleaned_data