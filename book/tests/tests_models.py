from django.test import TestCase
from ..models import BookCover, Barber

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

