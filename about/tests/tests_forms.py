from django.test import TestCase
from about.forms import CollaborationForm
from about.models import Collaboration


class CollaborationFormTest(TestCase):
    def test_valid_form(self):
        """Test if the form is valid with correct data."""
        form_data = {
            'barber_name': 'Zaki Nor',
            'barber_shop': 'Sockenvägen 3A',
            'business_type': 'barber',
            'service_offered': 'Haircut, Beard Trim',
            'email': 'zaki@example.com',
            'number': '1234567890',
            'more_info': 'Looking forward to collaborating!',
        }
        form = CollaborationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_fields(self):
        """Test if the form is invalid when required fields are missing."""
        form_data = {
            'barber_name': '',  # Missing required field
            'barber_shop': 'Sockenvägen 3A',
            'business_type': 'barber',
            'service_offered': 'Haircut, Beard Trim',
            'email': 'zaki@example.com',
            'number': '1234567890',
        }
        form = CollaborationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('barber_name', form.errors)

    def test_invalid_form_duplicate_entry(self):
        """Test if the form prevents duplicate barber name and shop entries."""

        # Create an existing entry
        Collaboration.objects.create(
            barber_name="Zaki Nor",
            barber_shop="Sockenvägen 3A",
            business_type="barber",
            service_offered="Haircut, Beard Trim",
            email="zaki@example.com",
            number="1234567890",
        )

        # Try submitting the same data again
        form_data = {
            'barber_name': "Zaki Nor",
            'barber_shop': "Sockenvägen 3A",
            'business_type': "barber",
            'service_offered': "Haircut, Beard Trim",
            'email': "zaki@example.com",
            'number': "1234567890",
        }
        form = CollaborationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('barber_name', form.errors)
