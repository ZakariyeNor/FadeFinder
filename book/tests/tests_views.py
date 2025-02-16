from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Barber, BookCover, BarberService, Booking
from datetime import datetime


class BookingFormViewTests(TestCase):
    """
    Test case for the booking form view.
    Tests the functionality of creating a booking using the booking form.
    """

    def setUp(self):
        """
        Set up the initial data for tests.
        Creates a user, a barber, a service, and a booking cover.
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='password'
        )
        self.barber = Barber.objects.create(
            barber_name="Test Barber",
            barber_address="Test Address",
            barber_number="123456789"
        )
        self.service = BarberService.objects.create(
            barber=self.barber,
            service_name="Haircut",
            service_price=20.00
        )
        self.cover = BookCover.objects.create(
            booking_intro="Welcome to our booking system"
        )
        self.url = reverse('book')

    def test_booking_form_post_valid(self):
        """
        Test posting a valid booking form.
        Ensures a booking is created and user is redirected to the 'book' page.
        """
        self.client.login(username='testuser', password='password')
        data = {
            'barber': self.barber.id,
            'service': self.service.id,
            'date': '2025-02-15',
            'time': '10:00:00'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(Booking.objects.count(), 1)
        booking = Booking.objects.first()
        self.assertEqual(booking.user, self.user)
        self.assertRedirects(response, reverse('book'))


class EditBookingViewTests(TestCase):
    """
    Test case for the edit booking view.
    Tests the functionality of editing a booking.
    """

    def setUp(self):
        """
        Set up the initial data for tests.
        Creates a user, a barber, a service, and a booking.
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='password'
        )
        self.other_user = User.objects.create_user(
            username='otheruser', password='password'
        )
        self.barber = Barber.objects.create(
            barber_name="Test Barber",
            barber_address="Test Address",
            barber_number="123456789"
        )
        self.service = BarberService.objects.create(
            barber=self.barber,
            service_name="Haircut",
            service_price=20.00
        )
        self.booking = Booking.objects.create(
            user=self.user,
            barber=self.barber,
            service=self.service,
            date='2025-02-15',
            time='10:00:00'
        )
        self.url = reverse(
            'edit_booking',
            kwargs={'booking_id': self.booking.id}
        )

    def test_edit_booking_view_logged_in(self):
        """
        Test accessing the edit booking view when the user is logged in.
        Ensures the correct context is available in the response.
        """
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertIn('booking', response.context)

    def test_edit_booking_post_valid(self):
        """
        Test posting a valid edit booking form.
        Ensures the booking is updated correctly and the user is redirected.
        """
        data = {
            'barber': self.barber.id,
            'service': self.service.id,
            'date': datetime.strptime('2025-02-16', '%Y-%m-%d').date(),
            'time': '11:00:00'
        }
        response = self.client.post(self.url, data)
        self.assertRedirects(response, reverse('book'))

    def test_edit_booking_view_permission_error(self):
        """
        Test that another user cannot edit another user's booking.
        Ensures proper permission handling.
        """
        self.client.login(username='otheruser', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('book'))


class DeleteBookingViewTests(TestCase):
    """
    Test case for the delete booking view.
    Tests the functionality of deleting a booking.
    """

    def setUp(self):
        """
        Set up the initial data for tests.
        Creates a user, a barber, a service, and a booking.
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='password'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            password='password'
        )
        self.barber = Barber.objects.create(
            barber_name="Test Barber",
            barber_address="Test Address",
            barber_number="123456789"
        )
        self.service = BarberService.objects.create(
            barber=self.barber,
            service_name="Haircut",
            service_price=20.00
        )
        self.booking = Booking.objects.create(
            user=self.user,
            barber=self.barber,
            service=self.service,
            date='2025-02-15',
            time='10:00:00'
        )
        self.url = reverse(
            'delete_booking',
            kwargs={'booking_id': self.booking.id}
        )

    def test_delete_booking_view_logged_in(self):
        """
        Test deleting a booking when the user is logged in.
        Ensures the booking is deleted and the user is redirected.
        """
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('book'))
        self.assertEqual(Booking.objects.count(), 0)

    def test_delete_booking_view_permission_error(self):
        """
        Test that another user cannot delete another user's booking.
        Ensures proper permission handling.
        """
        self.client.login(username='otheruser', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('book'))
