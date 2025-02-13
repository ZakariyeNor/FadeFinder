from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import BookCover, Booking, Barber, BarberService
from .forms import BookingForm


#View for the booking form
def booking_form(request):
    """ Diplay the booking form with barber and service """

    barbers = Barber.objects.all() 
    cover = BookCover.objects.first()
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user)
    else:
        bookings = []
    
    
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
            "bookings": bookings,
        },
    )


#Create view for the edit booking 
def edit_booking(request, booking_id):
    booked = get_object_or_404(Booking, id=booking_id)

    if booked.user != request.user:
        messages.add_message(
            request, messages.ERROR,
            "You are not allowed to edit this booking!")
        return redirect('book')

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booked)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'You updated the appointment successfully!'
            )
            return redirect('book')
            
        else:
            messages.add_message(
                request, messages.ERROR,
                'You need to choose available time based on the service and barber!'
            )
    else:
        form = BookingForm(instance=booked)

    return render(
        request,
        'book/edit_booking.html',
        {
            "form": form,
            "booking": booked,
        }
        )


#Create view for the delete booking 
def delete_booking(request, booking_id):
    booked = get_object_or_404(Booking, id=booking_id)

    if booked.user == request.user:
        booked.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'You Deleted the appointment successfully!'
        )
        return redirect('book')
            
    else:
        messages.add_message(
            request, messages.ERROR,
            'You need to choose your own appoinments to delete!'
        )
    return redirect('book')