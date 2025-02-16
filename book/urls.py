from django.urls import path
from . import views

#Booking app path
urlpatterns = [
    path('form/', views.booking_form, name='book'),
    path(
        'edit_booking/<int:booking_id>/', views.edit_booking,
        name='edit_booking'
    ),
    path
    ('delete_booking/<int:booking_id>', views.delete_booking,
    name='delete_booking'
    ),
]