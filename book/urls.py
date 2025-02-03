from django.urls import path
from . import views

#Booking app path
urlpatterns = [
    path('', views.BookCoverShow.as_view(), name='book'),
    path('booking', views.booking_view, name='booking_form'),
]