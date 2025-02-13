from django.test import TestCase
from .models import Booking
from .forms import BookingForm
from .models import Booking
from datetime import date, datetime

# Create your tests here.
class TestDateinput(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.form = BookingForm()


    def tearDown(self):
        self.form = None


