from django.shortcuts import render
from django.views import generic
from .models import BookCover

# Create your views here.
class BookCoverShow(generic.ListView):
    model = BookCover
    template_name = 'book/booking.html'
    context_object_name = 'bookingcover'


