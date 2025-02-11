from django import forms
from .models import Collaboration, ContactUs

# Collaboration form
class CollaborationForm(forms.ModelForm):
    class Meta:
        model = Collaboration
        fields = ('barber_name', 'barber_shop', 'business_type', 'service_offered', 'email', 'number', 'more_info',)

    
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

        #check if the combination of barber name and barbershop already exists
        if barber_name and barber_shop:
            if Collaboration.objects.filter(barber_name=barber_name, barber_shop=barber_shop).exists():
                self.add_error('barber_shop', 'A collaboration with this barber name and shop already exists.')
        return cleaned_data

# ContactUs form
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'phone', 'email', 'message',)

        name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'placeholder': 'Enter Your Name'
                }
            )
        )

        phone = forms.CharField(
            widget=forms.NumberInput(
                attrs={
                    'placeholder': 'Enter Your Number'
                }
            )
        )

        email = forms.CharField(
            widget=forms.EmailField(
                attrs={
                    'placeholder': 'Enter Your Email'
                }
            )
        )

        message = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    'placeholder': 'Type your message here...'
                }
            )
        )

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get('email')
        message = cleaned_data.get('message')

    # Check if the user already sent same message with same email
    if email and message:
        if ContactUs.objects.filter(email=email, message=message).exists():
            self.add_error(
                'message', 'A similar message has already been sent. Please modify your message if you need to add more details.'
            )
    return