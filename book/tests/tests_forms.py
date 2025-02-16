from django.test import TestCase
from ..forms import DateInput, TimeInput, BookingForm
from ..models import Booking, Barber, BarberService
from datetime import date, datetime


class TestDateInput(TestCase):

    def setUp(self):
        self.date_input = DateInput()

    def test_form_is_valid(self):
        self.assertEqual(self.date_input.input_type, 'date')
        today_str = date.today().strftime('%Y-%m-%d')
        self.assertEqual(self.date_input.attrs.get('today'), today_str)

    def tearDown(self):
        pass


class TestTimeInput(TestCase):

    def setUp(self):
        self.time_input = TimeInput()

    def test_input_type(self):
        self.assertEqual(self.time_input.input_type, 'time')

    def test_min_attribute(self):
        current_time = datetime.now().strftime('%H:%M')
        self.assertEqual(self.time_input.attrs.get('min'), current_time)

    def tearDown(self):
        pass


class TestBookingForm(TestCase):

    def setUp(self):
        self.barber = Barber.objects.create(
            barber_name='Zaki Nor',
            barber_address='Sockenvägen 3A',
            barber_number='1234567890'
        )
        self.service = BarberService.objects.create(
            barber=self.barber,
            service_name='Haircut',
            service_price=20.00
        )

    def test_form_is_valid(self):
        form_data = {
            'barber': self.barber.id,
            'service': self.service.id,
            'date': date.today().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M'),
        }
        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_no_barber(self):
        form_data = {
            'service': self.service.id,
            'date': date.today().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M'),
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('barber', form.errors)

    def test_form_invalid_no_service(self):
        form_data = {
            'barber': self.barber.id,
            'date': date.today().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M'),
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('service', form.errors)

    def test_form_has_correct_fields(self):
        form = BookingForm()
        self.assertIn('barber', form.fields)
        self.assertIn('service', form.fields)
        self.assertIn('date', form.fields)
        self.assertIn('time', form.fields)

    def test_form_date_input_value(self):
        form = BookingForm()
        self.assertEqual(
            form.fields['date'].widget.attrs['today'],
            date.today().strftime('%Y-%m-%d')
        )

    def test_form_time_input_min_value(self):
        form = BookingForm()
        self.assertEqual(
            form.fields['time'].widget.attrs['min'],
            datetime.now().strftime('%H:%M')
        )

    def tearDown(self):
        pass
