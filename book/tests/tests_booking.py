from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from unittest.mock import MagicMock

class BookingPageTestCase(TestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Simulate bookings for an authenticated user
        self.booking = MagicMock()
        self.booking.service.service_name = 'Haircut'
        self.booking.time = '10:00 AM'
        self.booking.barber.barber_name = 'Barber A'
        self.booking.service.service_price = '20'
        self.booking.date = '2025-02-15'
        self.booking.user = self.user

    def test_authenticated_user_sees_booking_form(self):
        """Test that an authenticated user sees the booking form."""
        # Log in as the user
        self.client.login(username='testuser', password='testpassword')
        
        # Render the template
        response = self.client.get(reverse('book'))
        
        # Capture the HTML output
        html_output = response.content.decode('utf-8')
        
        # Write the HTML output to a file
        with open('book/tests/output_book.html', 'w', encoding='utf-8') as f:
            f.write(html_output)

        # Assertions
        self.assertContains(response, '<form')  # Check if the form is present
        self.assertContains(response, '<input type="hidden" name="csrfmiddlewaretoken"')  # Ensure CSRF token is present

    def test_delete_booking_modal_present_for_authenticated_user(self):
        """Test that an authenticated user sees the delete booking modal."""
        # Log in as the user
        self.client.login(username='testuser', password='testpassword')
        
        # Create bookings context with booking and pass to the response
        bookings = [self.booking]
        response = self.client.get(reverse('book'), {'bookings': bookings})
        
        # Check that the delete modal is present in the rendered HTML
        self.assertContains(response, 'Confirm Deletion')
