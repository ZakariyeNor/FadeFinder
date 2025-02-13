from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..admin import BookCoverAdmin
from ..models import BookCover, Barber


class TestBookCoverAdmin(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create a user and BookCover instance for admin tests."""
        cls.user = User.objects.create_user(
            username='adminusername', password='adminpassword'
        )
        
        cls.book_cover = BookCover.objects.create(
            booking_intro="Welcome to (barber shop name)."
        )

    def setUp(self):
        """Log in the admin user for each test."""
        self.client.login(username='zacki', password='zaki1234')

    def test_book_cover_admin_registration(self):
        """Test that the 'BookCover' model is registered in the admin site."""
        from django.contrib import admin
        self.assertIn(BookCover, admin.site._registry)

    def test_admin_can_edit_book_cover(self):
        """Test that the admin can edit the 'booking_intro' field."""
        new_content = "Updated introduction content for the booking page."
        
        response = self.client.post(
            reverse('admin:book_bookcover_change', args=[self.book_cover.id]),
            {'booking_intro': new_content},
            follow=True
        )

class TestBarberAdmin(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create a user and Barber instance for admin tests."""
        cls.user = User.objects.create_user(
            username='adminusername', password='adminpassword'
        )
        
        # Create Barber instances with the given details
        cls.zaki_nor = Barber.objects.create(
            barber_name='Zaki Nor',
            barber_address='Sockenvägen 3A',
            barber_number='1234567890'
        )
        cls.mccall_ali = Barber.objects.create(
            barber_name='McCall Ali',
            barber_address='Central Bank 12B',
            barber_number='0987654321'
        )

    def test_barber_admin_registration(self):
        """Test that the 'Barber' model is registered in the admin site."""
        from django.contrib import admin
        self.assertIn(Barber, admin.site._registry)

    
