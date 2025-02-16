from django.test import TestCase
from django.contrib.admin.sites import site
from ..models import BarberInfo, ServicesDes
from ..admin import BarberInfoAdmin, ServicesDesAdmin


# Create your tests here.
# Barber admin tests
class BarberInfoAdminTest(TestCase):

    def test_admin_registration(self):
        # Ensure BarberInfo is registered in Django admin
        self.assertIn(BarberInfo, site._registry)

    def test_admin_list_display(self):
        # Verify that list_display is correctly set
        admin_instance = BarberInfoAdmin(BarberInfo, site)
        self.assertEqual(admin_instance.list_display, (
            'title', 'created_on', 'updated_on'
            )
        )

    def test_admin_search_fields(self):
        # Verify that search_fields is correctly set
        admin_instance = BarberInfoAdmin(BarberInfo, site)
        self.assertEqual(admin_instance.search_fields, ('title',))

    def test_admin_summernote_fields(self):
        # Verify that summernote_fields is correctly set
        admin_instance = BarberInfoAdmin(BarberInfo, site)
        self.assertEqual(admin_instance.summernote_fields, ('description',))


# Service admin test
class ServicesDesAdminTest(TestCase):

    def test_admin_registration(self):
        # Ensure ServicesDes is registered in Django admin
        self.assertIn(ServicesDes, site._registry)

    def test_admin_list_display(self):
        # Verify that list_display is correctly set
        admin_instance = ServicesDesAdmin(ServicesDes, site)
        self.assertEqual(admin_instance.list_display, (
            'title', 'created_on', 'updated_on'
            )
        )

    def test_admin_search_fields(self):
        # Verify that search_fields is correctly set
        admin_instance = ServicesDesAdmin(ServicesDes, site)
        self.assertEqual(admin_instance.search_fields, ('title',))

    def test_admin_summernote_fields(self):
        # Verify that summernote_fields is correctly set
        admin_instance = ServicesDesAdmin(ServicesDes, site)
        self.assertEqual(admin_instance.summernote_fields, ('description',))
