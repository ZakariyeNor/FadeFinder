from django.shortcuts import render
from django.views import generic
from .models import BarberInfo, ServicesDes
from book.models import Booking


# Create your views here.
class BarberInfoContent(generic.ListView):
    model = BarberInfo
    template_name = 'home/home.html'
    context_object_name = 'barberinfo'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicedescription'] = ServicesDes.objects.all()
        
        #Get bookings for the logged-in user
        if self.request.user.is_authenticated:
            context['bookings'] = Booking.objects.filter(user=self.request.user)
        else:
            context['bookings'] = []

        return context
