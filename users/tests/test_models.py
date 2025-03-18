from django.test import TestCase

from users.models import User


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="G2l3l@example.com",
            password="password",
            first_name="John",
            last_name="Doe",
        )

    # test create normal not admin user
    def test_create_user(self):
        self.assertEqual(self.user.email, "G2l3l@example.com")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertFalse(self.user.is_admin)

    # test create admin user
    def test_create_superuser(self):
        self.user.is_admin = True
        self.user.save()
        self.assertTrue(self.user.is_admin)
        self.assertEqual(self.user.email, "G2l3l@example.com")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_user_str(self):
        self.assertEqual(str(self.user), "G2l3l@example.com")
