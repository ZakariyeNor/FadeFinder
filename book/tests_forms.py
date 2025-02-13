from django.test import TestCase
from .forms import DateInput, TimeInput, BookingForm
from .models import Booking, Barber, BarberService
from datetime import date, datetime


# DateInput Test
class TestDateInput(TestCase):
    def setUp(self):
        """Runs before each individual test."""
        self.date_input = DateInput()  # Create an instance of DateInput

    def test_form_is_valid(self):
        """Test that the input_type is 'date' and 'today' is set correctly."""
        # Verify that the input_type is set to 'date'
        self.assertEqual(self.date_input.input_type, 'date')

        # Verify that the 'today' attribute is set correctly
        today_str = date.today().strftime('%Y-%m-%d')
        self.assertEqual(self.date_input.attrs.get('today'), today_str)

    def tearDown(self):
        """Runs after each individual test."""
        pass

# TimeInput Test
class TestTimeInput(TestCase):
    def setUp(self):
        """Runs before each individual test."""
        self.time_input = TimeInput()

    def test_input_type(self):
        """Test that the input_type is correctly set to 'time'."""
        self.assertEqual(self.time_input.input_type, 'time')

    def test_min_attribute(self):
        """Test that the 'min' attribute is set to the current time."""
        # Get the current time formatted as '%H:%M'
        current_time = datetime.now().strftime('%H:%M')
        self.assertEqual(self.time_input.attrs.get('min'), current_time)

    def tearDown(self):
        """Runs after each individual test."""
        pass

#Booking form test
class TestBookingForm(TestCase):
    # Runs before each individual test
    def setUp(self):
        print("Setting up the individual test.")
        
        # Creating instances of the model to be used in the form
        self.barber = Barber.objects.create(
            barber_name='John Doe',
            barber_address='123 Barber Street',
            barber_number='1234567890'
        )
        self.service = BarberService.objects.create(
            barber=self.barber,
            service_name='Haircut',
            service_price=20.00
        )
    
    def test_form_is_valid(self):
        """Test that the form is valid when correct data is provided."""
        # Valid data for the form
        form_data = {
            'barber': self.barber.id,
            'service': self.service.id,
            'date': date.today().strftime('%Y-%m-%d'),  # Today's date
            'time': datetime.now().strftime('%H:%M'),  # Current time
        }
        
        # Create an instance of the form with valid data
        form = BookingForm(data=form_data)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_form_invalid_no_barber(self):
        """Test that the form is invalid when no barber is provided."""
        # Invalid data for the form (missing barber)
        form_data = {
            'service': self.service.id,
            'date': date.today().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M'),
        }

        # Create an instance of the form with invalid data
        form = BookingForm(data=form_data)

        # Check if the form is invalid
        self.assertFalse(form.is_valid())
        self.assertIn('barber', form.errors)  # Ensure the error is related to the missing barber

    def test_form_invalid_no_service(self):
        """Test that the form is invalid when no service is provided."""
        # Invalid data for the form (missing service)
        form_data = {
            'barber': self.barber.id,
            'date': date.today().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M'),
        }

        # Create an instance of the form with invalid data
        form = BookingForm(data=form_data)

        # Check if the form is invalid
        self.assertFalse(form.is_valid())
        self.assertIn('service', form.errors)  # Ensure the error is related to the missing service

    def test_form_has_correct_fields(self):
        """Test that the form contains the correct fields."""
        form = BookingForm()

        # Check if the form has the correct fields
        self.assertIn('barber', form.fields)
        self.assertIn('service', form.fields)
        self.assertIn('date', form.fields)
        self.assertIn('time', form.fields)

    def test_form_date_input_value(self):
        """Test that the date input value is today's date."""
        form = BookingForm()

        # Check that the date input field has today's date as its value
        self.assertEqual(form.fields['date'].widget.attrs['today'], date.today().strftime('%Y-%m-%d'))

    def test_form_time_input_min_value(self):
        """Test that the time input 'min' attribute is set to the current time."""
        form = BookingForm()

        # Check that the time input field has the correct 'min' attribute
        self.assertEqual(form.fields['time'].widget.attrs['min'], datetime.now().strftime('%H:%M'))

    # Runs after each individual test
    def tearDown(self):
        print("Tearing down the individual test.")
