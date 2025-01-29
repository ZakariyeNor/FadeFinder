from django.shortcuts import render
from django.views import generic
from .models import BarberInfo


# Create your views here.
class BarberInfoContent(generic.ListView):
    model = BarberInfo
    template_name = 'home/home.html'
    context_object_name = 'barberinfo'
