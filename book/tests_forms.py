from django.test import TestCase
from .forms import DateInput
from datetime import date

#Runs once before all test
@classmethod
def setUpClass(cls):
    print("Setting up the test class.")

#Runs once after all test
@classmethod
def tearDownClass(cls):
    print("Tearing down the test class.")


#Dateinput test
class TestDateInput(TestCase):

    def test_form_is_valid(self):
        # Create an instance of DateInput
        date_input = DateInput()

        # Verify that the input_type is set to 'date'
        self.assertEqual(date_input.input_type, 'date')

        # Verify that the 'today' attribute is set correctly
        today_str = date.today().strftime('%Y-%m-%d')