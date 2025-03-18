from django.test import TestCase

from users.models import User
from users.serializers import UserCreateSerializer, UserSerializer


class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="G2l3l@example.com",
            password="password",
            first_name="John",
            last_name="Doe",
        )

    def test_user_create_serializer(self):
        serializer = UserCreateSerializer(instance=self.user)
        data = serializer.data
        self.assertEqual(data["email"], "G2l3l@example.com")
        self.assertEqual(data["first_name"], "John")
        self.assertEqual(data["last_name"], "Doe")

    def test_user_serializer(self):
        serializer = UserSerializer(instance=self.user)
        data = serializer.data
        self.assertEqual(data["email"], "G2l3l@example.com")
        self.assertEqual(data["first_name"], "John")
        self.assertEqual(data["last_name"], "Doe")
