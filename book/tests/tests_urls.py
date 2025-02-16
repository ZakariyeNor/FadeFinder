from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from ..models import Barber, BarberService, Booking

# he correctness of your URL patterns and the behavior
# of the views
# Test for booking form url


class BookingFormUrlTests(TestCase):
    def test_booking_form_url(self):
        """Test if the booking form URL is resolved correctly"""
        url = reverse('book')
        self.assertEqual(url, '/book/form/')


# test ensures that the URL for editing a
# booking correctly resolves to the edit_booking view.
class EditBookingUrlTests(TestCase):
    def test_edit_booking_url(self):
        """Test if the edit booking URL
        is resolved correctly with booking_id"""
        booking_id = 1
        url = reverse('edit_booking', kwargs={'booking_id': booking_id})
        self.assertEqual(url, f'/book/edit_booking/{booking_id}/')


# This test checks if the URL for deleting a
# booking correctly resolves to the delete_booking view.
class DeleteBookingUrlTests(TestCase):
    def test_delete_booking_url(self):
        """Test if the delete booking URL
        is resolved correctly with booking_id"""
        booking_id = 1
        url = reverse('delete_booking', kwargs={'booking_id': booking_id})
        self.assertEqual(url, f'/book/delete_booking/{booking_id}')
