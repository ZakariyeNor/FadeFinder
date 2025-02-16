from django.test import TestCase
from ..models import BarberInfo, ServicesDes
from django.utils import timezone

# Create your tests here.
# Barber modal test


class BarberInfoModelTest(TestCase):
    def test_barberinfo_creation(self):
        #  Create a new instance of the BarberInfo model
        barber = BarberInfo.objects.create(
            title="Test Barber",
            description="A description for the test barber.",
            created_on=timezone.now(),
            updated_on=timezone.now()
        )

        #  Check if the BarberInfo instance is saved and can be retrieved
        self.assertEqual(barber.title, "Test Barber")
        self.assertEqual(
            barber.description, "A description for the test barber."
        )
        self.assertTrue(isinstance(barber, BarberInfo))
        self.assertEqual(str(barber), "Created by | Test Barber")

    def test_barberinfo_default_image(self):
        #  Test if the default image is applied correctly
        barber = BarberInfo.objects.create(
            title="Test Barber 2",
            description="Another description for the test barber.",
            created_on=timezone.now(),
            updated_on=timezone.now()
        )

        self.assertEqual(barber.image, "placeholder")


# Test for service modal
class ServicesDesModelTest(TestCase):

    def test_servicesdes_creation(self):
        #  Create a new instance of the ServicesDes model
        service = ServicesDes.objects.create(
            title="Haircut Service",
            services="A detailed description of"
            "the haircut service offered by the barber.",
            created_on=timezone.now(),
            updated_on=timezone.now()
        )

        #  Check if the ServicesDes instance is saved and can be retrieved
        self.assertEqual(service.title, "Haircut Service")
        self.assertEqual(
            service.services,
            "A detailed description of the"
            "haircut service offered by the barber."
        )
        self.assertTrue(isinstance(service, ServicesDes))
        self.assertEqual(str(service), "Haircut Service")

    def test_servicesdes_default_image(self):
        #  Test if the default image is applied correctly
        service = ServicesDes.objects.create(
            title="Shaving Service",
            services="A detailed description"
            "of the shaving service offered by the barber.",
            created_on=timezone.now(),
            updated_on=timezone.now()
        )

        self.assertEqual(service.image, "placeholder")
