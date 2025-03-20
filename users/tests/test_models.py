from django.test import TestCase

from users.models import Profile, User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="testpass123",
            first_name="Test",
            last_name="User",
        )

    def test_user_fields(self):
        """Test that the user fields have expected default values."""
        self.assertEqual(self.user.first_name, "Test")
        self.assertEqual(self.user.last_name, "User")
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_admin)
        self.assertEqual(self.user.email, "testuser@example.com")

    def test_email_address_required(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email="", password="testpass123", first_name="Test", last_name="User"
            )

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(
            email="superuser@example",
            password="testpass123",
            first_name="Super",
            last_name="User",
        )
        self.assertTrue(superuser.is_admin)

    def test_str_representation(self):
        expected_str = f"{self.user.email}"
        self.assertEqual(str(self.user), expected_str)

    def test_has_perm(self):
        self.assertTrue(self.user.has_perm("users.view_user"))

    def test_has_module_perms(self):
        self.assertTrue(self.user.has_module_perms("users"))

    def test_is_staff(self):
        self.user.is_admin = True
        self.assertTrue(self.user.is_staff)


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="profile@example.com",
            password="testpass123",
            first_name="Profile",
            last_name="User",
        )
        # Assume the profile is automatically created by a signal.
        self.profile = Profile.objects.get(user=self.user)

    def test_profile_fields(self):
        """Test that the profile fields have expected default values."""
        self.assertEqual(self.profile.age, 0)  # default
        self.assertEqual(self.profile.address, "")
        self.assertEqual(self.profile.phone_number, "")

    def test_str_representation(self):
        """Test the string representation of the profile."""
        expected_str = f"{self.user.first_name} {self.user.last_name}"
        self.assertEqual(str(self.profile), expected_str)
