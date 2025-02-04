from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import generic
from django.contrib import messages
from .models import BookCover, Booking, Barber, BarberService
from .forms import BookingForm

# Create your views here.
class BookCoverShow(generic.ListView):
    model = BookCover
    template_name = 'book/booking_form.html'
    context_object_name = 'bookingcover'

    

#View for the booking form
def booking_form_view(request):
    """ Diplay the booking form with barber and service """

    barbers = Barber.objects.all() 
    
    if request.method == "POST":
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.add_message(request, messages.SUCCESS,
            'You booked an appointment successfully!')
            return redirect('book')

        else:
            messages.add_message(request, messages.ERROR,
            "Couldn't book an appointment. Please try again.")
    else:
        form = BookingForm()
        
    return render(
        request,
        "book/booking_form.html",
        {
            "barbers": barbers,
            "form": form
        },
    )
