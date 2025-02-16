from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import admin
from ..models import BookCover, Barber, BarberService, Booking


class TestBookCoverAdmin(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='adminusername', password='adminpassword'
        )
        cls.book_cover = BookCover.objects.create(
            booking_intro="Welcome to (barber shop name)."
        )

    def setUp(self):
        self.client.login(username='zacki', password='zaki1234')

    def test_book_cover_admin_registration(self):
        self.assertIn(BookCover, admin.site._registry)

    def test_admin_can_edit_book_cover(self):
        new_content = "Updated introduction content for the booking page."
        response = self.client.post(
            reverse('admin:book_bookcover_change', args=[self.book_cover.id]),
            {'booking_intro': new_content},
            follow=True
        )
        self.assertEqual(response.status_code, 200)


class TestBarberAdmin(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='adminusername', password='adminpassword'
        )
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
        self.assertIn(Barber, admin.site._registry)


class TestBarberServiceAdmin(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.admin_user = User.objects.create_superuser(
            username='adminuser', password='adminpassword'
        )
        cls.zaki_nor = Barber.objects.create(
            barber_name='Zaki Nor',
            barber_address='Sockenvägen 3A',
            barber_number='1234567890'
        )
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
        self.assertIn(BarberService, admin.site._registry)

    def test_barber_service_admin_list_display(self):
        self.client.login(username='adminuser', password='adminpassword')
        response = self.client.get(
            reverse('admin:book_barberservice_changelist')
        )
        self.assertContains(response, 'Haircut')
        self.assertContains(response, '15.00')
        self.assertContains(response, 'Shave')
        self.assertContains(response, '10.00')

    def test_barber_service_admin_search(self):
        self.client.login(username='adminuser', password='adminpassword')
        response = self.client.get(
            reverse('admin:book_barberservice_changelist') + '?q=Haircut'
        )
        self.assertContains(response, 'Haircut')
        self.assertNotContains(response, 'Shave')

    def test_barber_service_str_representation_in_admin(self):
        self.client.login(username='adminuser', password='adminpassword')
        response = self.client.get(
            reverse('admin:book_barberservice_change', args=[self.service1.id])
        )
        self.assertContains(response, 'Haircut')


class TestBookingAdmin(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.admin_user = User.objects.create_superuser(
            username='adminuser', password='adminpassword'
        )
        cls.barber = Barber.objects.create(
            barber_name='Zaki Nor',
            barber_address='Sockenvägen 3A',
            barber_number='1234567890'
        )
        cls.service = BarberService.objects.create(
            barber=cls.barber,
            service_name='Haircut',
            service_price=15.00
        )
        cls.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        cls.booking = Booking.objects.create(
            user=cls.user,
            barber=cls.barber,
            service=cls.service,
            date='2025-02-14',
            time='14:00:00'
        )

    def test_booking_admin_registration(self):
        self.assertIn(Booking, admin.site._registry)

    def test_booking_admin_list_filter(self):
        self.client.login(username='adminuser', password='adminpassword')
        response = self.client.get(reverse('admin:book_booking_changelist'))
        self.assertContains(response, 'User')
        self.assertContains(response, 'Barber')
        self.assertContains(response, 'Service')
        self.assertContains(response, 'Date')
        self.assertContains(response, 'Time')

    def test_booking_admin_add_form(self):
        self.client.login(username='adminuser', password='adminpassword')
        response = self.client.get(reverse('admin:book_booking_add'))
        self.assertContains(response, 'User')
        self.assertContains(response, 'Barber')
        self.assertContains(response, 'Service')
        self.assertContains(response, 'Date')
        self.assertContains(response, 'Time')
