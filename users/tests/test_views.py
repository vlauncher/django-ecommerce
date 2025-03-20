from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import Profile

User = get_user_model()


class ProfileViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="profile@example.com",
            password="testpass123",
            first_name="Profile",
            last_name="User",
        )
        # Assume the profile is automatically created by a signal.
        self.profile = Profile.objects.get(user=self.user)
        self.client.force_authenticate(user=self.user)

    def test_get_profile(self):
        response = self.client.get(f"/api/v1/auth/profiles/{self.profile.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_profile(self):
        data = {"age": 30, "address": "123 Main St", "phone_number": "555-555-5555"}
        response = self.client.put(f"/api/v1/auth/profiles/{self.profile.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["age"], 30)
        self.assertEqual(response.data["address"], "123 Main St")
        self.assertEqual(response.data["phone_number"], "555-555-5555")
