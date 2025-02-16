from django import forms
from .models import Collaboration
from django.core.exceptions import ValidationError


# Collaboration form
class CollaborationForm(forms.ModelForm):
    class Meta:
        model = Collaboration
        fields = (
            'barber_name',
            'barber_shop', 'business_type',
            'service_offered', 'email',
            'number', 'more_info',
        )

    barber_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Your Name'
            }
        )
    )

    barber_shop = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Barber Shop Name'
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter Your Email'
            }
        )
    )

    number = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Enter Your Number'
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()

        barber_name = cleaned_data.get('barber_name')
        barber_shop = cleaned_data.get('barber_shop')

        # You can optionally add errors to both fields
        if barber_name and barber_shop:
            if Collaboration.objects.filter(
                barber_name=barber_name,
                barber_shop=barber_shop
            ).exists():
                self.add_error(
                    'barber_name', 'A collaboration with'
                    'this barber name and shop already exists.'
                )

        return cleaned_data
