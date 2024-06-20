from rest_framework import serializers
from django.contrib.auth.models import User
import time


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для класса User
    """

    class Meta:
        model = User
        fields = ["username", "password", "email"]
