
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from accounts.models import User
from main.models import TimeLog

"""Serializes and Deserializes the User Model"""
class UserSerializer(serializers.ModelSerializer):
    employee_id = serializers.CharField(source="username")
    is_clocked_in = serializers.SerializerMethodField("_get_clocked_in_status")

    def _get_clocked_in_status(self, instance):
        try:
            timelog = TimeLog.objects.order_by("-id").first()
            if timelog.time_out:
                return True
            else:
                return False
        except:
            return False
     
    class Meta:
        fields = ["id", "employee_id", "first_name", "last_name", "is_clocked_in"]
        model = User
