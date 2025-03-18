from django.test import TestCase
from rest_framework.test import APIClient

from users.models import User


class UserViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="password",
            first_name="Test",
            last_name="User",
        )
