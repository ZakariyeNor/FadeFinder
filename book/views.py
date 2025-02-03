from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from .models import BookCover, Booking
from .forms import BookingForm

# Create your views here.
class BookCoverShow(generic.ListView):
    model = BookCover
    template_name = 'book/booking.html'
    context_object_name = 'bookingcover'


#View for the booking form
def booking_view(request):
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.save()
            messages.add_message(request, messages.SUCCESS,
            'You booked an appointment successfully!')
            return redirect('booking.html')

        else:
            messages.add_message(request, messages.ERROR,
            "Couldn't book an appointment. Please try again.")
    else:
        booking_form = BookingForm()
        
    return render(
        request,
        "book/booking.html",
        {"booking_form": booking_form}, 
    )



