from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..admin import BookCoverAdmin
from ..models import BookCover, Barber, BarberService, Booking

#Test for bookcover admin
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


#Test for BarberAdmin admin
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

    
#Test for BarberService admin
class TestBarberServiceAdmin(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Create user, Barber, and BarberService instances for admin tests."""
        # Create a user for admin login
        cls.admin_user = User.objects.create_superuser(
            username='adminuser', password='adminpassword'
        )
        
        # Create a Barber instance
        cls.zaki_nor = Barber.objects.create(
            barber_name='Zaki Nor',
            barber_address='Sockenvägen 3A',
            barber_number='1234567890'
        )
        
        # Create BarberService instances
        cls.service1 = BarberService.objects.create(
            barber=cls.zaki_nor,
            service_name='Haircut',
            service_price=15.00
        )
        
        cls.service2 = BarberService.objects.create(
            barber=cls.zaki_nor,
            service_name='Shave',
            service_price=10.00
        )

    def test_barber_service_admin_registration(self):
        """Test that the 'BarberService' model is registered in the admin site."""
        from django.contrib import admin
        self.assertIn(BarberService, admin.site._registry)

    def test_barber_service_admin_list_display(self):
        """Test that the 'service_name' and 'service_price' fields are displayed in the admin list view."""
        # Login as the admin user
        self.client.login(username='adminuser', password='adminpassword')
        
        # Access the BarberService change list page
        response = self.client.get(reverse('admin:book_barberservice_changelist'))
        
        # Check if the 'service_name' and 'service_price' are correctly displayed in the list view
        self.assertContains(response, 'Haircut')
        self.assertContains(response, '15.00')
        self.assertContains(response, 'Shave')
        self.assertContains(response, '10.00')

    def test_barber_service_admin_search(self):
        """Test that the search functionality works for the 'service_name' field."""
        # Login as the admin user
        self.client.login(username='adminuser', password='adminpassword')
        
        # Access the search results by searching for "Haircut"
        response = self.client.get(reverse('admin:book_barberservice_changelist') + '?q=Haircut')
        
        # Check if the search results contain the service
        self.assertContains(response, 'Haircut')
        self.assertNotContains(response, 'Shave')

    
    def test_barber_service_str_representation_in_admin(self):
        """Test that the string representation of the BarberService instance is correctly shown in the admin."""
        # Login as the admin user
        self.client.login(username='adminuser', password='adminpassword')
        
        # Access the change page for the first BarberService instance
        response = self.client.get(reverse('admin:book_barberservice_change', args=[self.service1.id]))
        
        # Check if the string representation is displayed
        self.assertContains(response, 'Haircut')


#Test for Booking admin
class TestBookingAdmin(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create user, Barber, BarberService, and Booking instances for admin tests."""
        # Create a superuser for admin login
        cls.admin_user = User.objects.create_superuser(
            username='adminuser', password='adminpassword'
        )
        
        # Create a Barber instance
        cls.barber = Barber.objects.create(
            barber_name='Zaki Nor',
            barber_address='Sockenvägen 3A',
            barber_number='1234567890'
        )
        
        # Create a BarberService instance
        cls.service = BarberService.objects.create(
            barber=cls.barber,
            service_name='Haircut',
            service_price=15.00
        )
        
        # Create a User for the booking
        cls.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        
        # Create a Booking instance
        cls.booking = Booking.objects.create(
            user=cls.user,
            barber=cls.barber,
            service=cls.service,
            date='2025-02-14',
            time='14:00:00'
        )

    def test_booking_admin_registration(self):
        """Test that the 'Booking' model is registered in the admin site."""
        from django.contrib import admin
        self.assertIn(Booking, admin.site._registry)

    def test_booking_admin_list_filter(self):
        """Test that the list filter works for 'user', 'barber', 'service', 'date', and 'time'."""
        # Login as the admin user
        self.client.login(username='adminuser', password='adminpassword')
        
        # Access the Booking change list page
        response = self.client.get(reverse('admin:book_booking_changelist'))
        
        # Check if the filter options are available in the response
        self.assertContains(response, 'User')
        self.assertContains(response, 'Barber')
        self.assertContains(response, 'Service')
        self.assertContains(response, 'Date')
        self.assertContains(response, 'Time')

    def test_booking_admin_add_form(self):
        """Test that the 'add' form for Booking is working."""
        # Login as the admin user
        self.client.login(username='adminuser', password='adminpassword')
        
        # Access the add form for the Booking model
        response = self.client.get(reverse('admin:book_booking_add'))
        
        # Check if the form contains the necessary fields
        self.assertContains(response, 'User')
        self.assertContains(response, 'Barber')
        self.assertContains(response, 'Service')
        self.assertContains(response, 'Date')
        self.assertContains(response, 'Time')
