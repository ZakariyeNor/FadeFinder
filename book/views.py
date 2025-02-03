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






