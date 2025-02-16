from django.shortcuts import render
from django.views import generic
from .models import BarberInfo, ServicesDes
from book.models import Booking


# Create your views here.
class BarberInfoContent(generic.ListView):
    """
    View that renders the barber information and service descriptions 
    for the homepage.

    This view inherits from `ListView` and retrieves a list of barber 
    information (`BarberInfo`) and service descriptions (`ServicesDes`).
    If the user is authenticated, it also retrieves the user's bookings 
    from the `Booking` model and includes them in the context.
    """

    model = BarberInfo
    template_name = 'home/home.html'
    context_object_name = 'barberinfo'

    def get_context_data(self, **kwargs):
        """
        Override the default method to add additional context, including
        service descriptions and user bookings if authenticated.
        """

        context = super().get_context_data(**kwargs)
        context['servicedescription'] = ServicesDes.objects.all()

        # Get bookings for the logged-in user
        if self.request.user.is_authenticated:
            context['bookings'] = Booking.objects.filter(
                user=self.request.user
            )
        else:
            context['bookings'] = []

        return context
