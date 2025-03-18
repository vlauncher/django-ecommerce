"""
Serializer for User model.
"""

from djoser.serializers import UserCreateSerializer, UserSerializer

from .models import User


class UserCreateSerializer(UserCreateSerializer):
    """
    Serializer for user creation.

    This serializer extends the default UserCreateSerializer to include
    additional fields for first name and last name.
    """

    class Meta(UserCreateSerializer.Meta):
        """
        Meta class for UserCreateSerializer.
        """

        model = User
        fields = ("email", "password", "first_name", "last_name")


class UserSerializer(UserSerializer):
    """
    Serializer for User model.

    """

    class Meta(UserSerializer.Meta):
        """
        Meta class for UserSerializer.
        """

        model = User
        fields = ("email", "first_name", "last_name")
