from django.test import TestCase
from about.models import About, Collaboration


# Create your tests here.
class AboutModelTest(TestCase):

    def setUp(self):
        """Set up a test instance of the About model."""
        self.about = About.objects.create(
            title="Test About",
            content="This is a test about me section."
        )

    def test_about_model_fields(self):
        """Test if the model fields are correctly set."""
        self.assertEqual(self.about.title, "Test About")
        self.assertEqual(
            self.about.content, "This is a test about me section.")
        self.assertIsNotNone(self.about.created_on)
        self.assertIsNotNone(self.about.updated_on)

    def test_about_model_str(self):
        """Test the __str__ method of the About model."""
        expected_str = f"{self.about.title} | {self.about.updated_on}"
        self.assertEqual(str(self.about), expected_str)


# Test for collaboration model
class CollaborationModelTest(TestCase):

    def setUp(self):
        """Set up a test instance of the Collaboration model."""
        self.collaboration = Collaboration.objects.create(
            barber_name="John Doe",
            barber_shop="Fade Haven",
            business_type="barber",
            service_offered="Hair Cutting",
            email="johndoe@email.com",
            number="1234567890",
            more_info="Open from 9am to 6pm",
        )

    def test_collaboration_model_fields(self):
        """Test if the model fields are correctly set."""
        self.assertEqual(self.collaboration.barber_name, "John Doe")
        self.assertEqual(self.collaboration.barber_shop, "Fade Haven")
        self.assertEqual(self.collaboration.business_type, "barber")
        self.assertEqual(self.collaboration.service_offered, "Hair Cutting")
        self.assertEqual(self.collaboration.email, "johndoe@email.com")
        self.assertEqual(self.collaboration.number, "1234567890")
        self.assertEqual(self.collaboration.more_info, "Open from 9am to 6pm")
        self.assertIsNotNone(self.collaboration.created_on)

    def test_collaboration_model_str(self):
        """Test the __str__ method of the Collaboration model."""
        expected_str = f"The {
            self.collaboration.barber_shop
            } owned by | {self.collaboration.barber_name}"
        self.assertEqual(str(self.collaboration), expected_str)

    def test_unique_constraint(self):
        """Test the unique constraint on barber_name and barber_shop fields."""
        with self.assertRaises(Exception):
            Collaboration.objects.create(
                barber_name="John Doe",
                barber_shop="Fade Haven",
                business_type="barber",
                service_offered="Hair Cutting",
                email="another@email.com",
                number="0987654321"
            )
