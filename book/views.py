from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import BookCover, Booking, Barber, BarberService
from .forms import BookingForm


#View for the booking form
def booking_form(request):
    """ Diplay the booking form with barber and service """

    barbers = Barber.objects.all() 
    cover = BookCover.objects.first()
    user_booked = Booking.objects.filter(user=request.user).exists() if request.user.is_authenticated else False
    
    if request.method == "POST":
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                'You booked an appointment successfully!')
            return redirect('book')

        else:
            messages.add_message(
                request, messages.ERROR,
                "Couldn't book an appointment. Please try again.")
    else:
        form = BookingForm()
        
    return render(
        request,
        "book/booking_form.html",
        {
            "barbers": barbers,
            "form": form,
            "bookcover": cover,
            "user_booked": user_booked,
        },
    )
