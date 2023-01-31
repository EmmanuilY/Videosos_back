from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'id')

class GoogleAuth(serializers.Serializer):
    """ Сериализация данных от Google
    """
    email = serializers.EmailField()
    token = serializers.CharField()
