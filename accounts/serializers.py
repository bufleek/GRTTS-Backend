
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    employee_id = serializers.CharField(source="username")
     
    class Meta:
        fields = ["id", "employee_id", "first_name", "last_name"]
        model = User


class ObtainTokenSerializer(TokenObtainPairSerializer):
    pass
