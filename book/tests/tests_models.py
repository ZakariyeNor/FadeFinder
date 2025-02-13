from django.test import TestCase
from django.contrib.auth.models import User
from ..models import BookCover, Barber, BarberService, Booking
from datetime import date, time


#Test for bookcover
class TestBookCoverModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Create a BookCover instance for all tests."""
        cls.book_cover = BookCover.objects.create(
            booking_intro="Welcome to our booking page!"
        )

    def test_book_cover_creation(self):
        """Test that a BookCover instance is created successfully."""
        self.assertEqual(BookCover.objects.count(), 1)

    def test_str_method(self):
        """Test the __str__ method returns the expected string."""
        self.assertEqual(str(self.book_cover), "Booking introduction")

    def test_booking_intro_max_length(self):
        """Test that the booking_intro field respects max_length."""
        max_length = self.book_cover._meta.get_field('booking_intro').max_length
        self.assertEqual(max_length, 200)


#Test for barbers 
class TestBarberModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Create a Barber instance for all tests."""
        cls.barber = Barber.objects.create(
            barber_name="Zaki Nor",
            barber_address="Sockenvägen 3A",
            barber_number="Sockenvägen 3A"
        )

    def test_barber_creation(self):
        """Test that a Barber instance is created successfully."""
        self.assertEqual(Barber.objects.count(), 1)

    def test_str_method(self):
        """Test that the __str__ method returns the barber's name."""
        self.assertEqual(str(self.barber), "Zaki Nor")

    def test_field_max_lengths(self):
        """Test max_length constraints on fields."""
        self.assertEqual(self.barber._meta.get_field("barber_name").max_length, 50)
        self.assertEqual(self.barber._meta.get_field("barber_address").max_length, 200)
        self.assertEqual(self.barber._meta.get_field("barber_number").max_length, 20)

    def test_ordering(self):
        """Test that the model ordering is by 'created_on'."""
        field_ordering = self.barber._meta.ordering
        self.assertEqual(field_ordering, ["created_on"])


#Testt for barber service's
class TestBarberServiceModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Create Barber and BarberService instances for all tests."""
        cls.barber = Barber.objects.create(
            barber_name="Zaki Nor",
            barber_address="Sockenvägen 3A",
            barber_number="Sockenvägen 3A"
        )

        cls.service = BarberService.objects.create(
            barber=cls.barber,
            service_name="Haircut",
            service_price=25.50
        )

    def test_service_creation(self):
        """Test that a BarberService instance is created successfully."""
        self.assertEqual(BarberService.objects.count(), 1)

    def test_str_method(self):
        """Test that the __str__ method returns the service name."""
        self.assertEqual(str(self.service), "Haircut")

    def test_field_max_lengths(self):
        """Test max_length constraint on service_name."""
        self.assertEqual(self.service._meta.get_field("service_name").max_length, 50)

    def test_service_price_constraints(self):
        """Test that the service price follows decimal field constraints."""
        field = self.service._meta.get_field("service_price")
        self.assertEqual(field.max_digits, 5)
        self.assertEqual(field.decimal_places, 2)

    def test_ordering(self):
        """Test that the model ordering is by 'created_on'."""
        field_ordering = self.service._meta.ordering
        self.assertEqual(field_ordering, ["created_on"])

    
class TestBookingModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Create User, Barber, BarberService, and Booking instances for all tests."""
        cls.user = User.objects.create_user(
            username='username', password='userpassword'
        )
        
        cls.barber = Barber.objects.create(
            barber_name="Zaki Nor",
            barber_address="Sockenvägen 3A",
            barber_number="Sockenvägen 3A"
        )

        cls.service = BarberService.objects.create(
            barber=cls.barber,
            service_name="Haircut",
            service_price=25.50
        )

        cls.booking = Booking.objects.create(
            user=cls.user,
            barber=cls.barber,
            service=cls.service,
            date=date.today(),
            time=time(15, 30)  # Setting time to 3:30 PM
        )

    def test_booking_creation(self):
        """Test that a Booking instance is created successfully."""
        self.assertEqual(Booking.objects.count(), 1)

    def test_str_method(self):
        """Test that the __str__ method returns the correct booking string."""
        self.assertEqual(str(self.booking), f"Booked by | {self.user}")

    def test_date_field(self):
        """Test that the date field is not null and has the correct type."""
        self.assertIsInstance(self.booking.date, date)

    def test_time_field(self):
        """Test that the time field is not null and has the correct type."""
        self.assertIsInstance(self.booking.time, time)

    def test_unique_time(self):
        """Test that the time field is unique."""
        with self.assertRaises(Exception):
            # Try to create a booking with the same time (should raise IntegrityError)
            Booking.objects.create(
                user=self.user,
                barber=self.barber,
                service=self.service,
                date=date.today(),
                time=self.booking.time  # try time uniqueness
            )

    def test_ordering(self):
        """Test that the model ordering is by 'updated_on' in descending order."""
        field_ordering = self.booking._meta.ordering