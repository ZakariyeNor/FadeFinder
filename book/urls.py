from django.urls import path
from . import views

#Booking app path
urlpatterns = [
    path('form/', views.booking_form, name='book'),
]