from django.contrib.admin.sites import site
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from about.models import About, Collaboration


class AboutAdminTest(TestCase):
    def setUp(self):
        """Set up a superuser and log in before running tests."""
        self.admin_user = User.objects.create_superuser(
            username="admin", password="adminpass", email="admin@example.com"
        )
        self.client.login(username="admin", password="adminpass")

        self.about = About.objects.create(
            title="Test About", content="This is a test", created_on="2024-02-13"
        )

    def test_about_admin_list_view(self):
        """Test if the About model appears correctly in the admin list view."""
        url = reverse("admin:about_about_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_admin_change_view(self):
        """Test if the About model can be accessed in the admin change view."""
        url = reverse("admin:about_about_change", args=[self.about.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_admin_add_view(self):
        """Test if we can create a new About instance from the admin."""
        url = reverse("admin:about_about_add")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_admin_permissions(self):
        """Test if a non-admin user is forbidden from accessing the admin."""
        self.client.logout()
        url = reverse("admin:about_about_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_summernote_widget(self):
        """Test if the Summernote widget is applied to the content field in the admin."""
        url = reverse("admin:about_about_add")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "summernote")


class CollaborationAdminTest(TestCase):
    def setUp(self):
        """Set up a superuser and a test Collaboration instance."""
        self.admin_user = User.objects.create_superuser(
            username="admin", password="adminpass", email="admin@example.com"
        )
        self.client.login(username="admin", password="adminpass")

        self.collaboration = Collaboration.objects.create(
            barber_name="Zaki Nor",
            barber_shop="Sockenvägen 3A",
            business_type="Salon",
            service_offered="Haircut",
            email="zaki@example.com",
            number="123456789",
            more_info="Experienced barber in Stockholm"
        )

    def test_collaboration_admin_list_view(self):
        """Test if the Collaboration model appears correctly in the admin list view."""
        url = reverse("admin:about_collaboration_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Zaki Nor")

    def test_collaboration_admin_change_view(self):
        """Test if the Collaboration model can be accessed in the admin change view."""
        url = reverse("admin:about_collaboration_change", args=[self.collaboration.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sockenvägen 3A")

    def test_collaboration_admin_add_view(self):
        """Test if the Collaboration model cannot be added due to readonly_fields."""
        url = reverse("admin:about_collaboration_add")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "readonly")

    def test_admin_permissions(self):
        """Test if a non-admin user is forbidden from accessing the Collaboration admin."""
        self.client.logout()
        url = reverse("admin:about_collaboration_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_collaboration_admin_search(self):
        """Test if search works properly in the admin."""
        url = reverse("admin:about_collaboration_changelist") + "?q=Zaki"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Zaki Nor")
