
from rest_framework import serializers

from accounts.models import User
from main.models import TimeLog
from main.serializers import OfficeSerializer, TimeLogSerializer

"""Serializes and Deserializes the User Model"""
class UserSerializer(serializers.ModelSerializer):
    employee_id = serializers.CharField(source="username")
    active_time_log = serializers.SerializerMethodField("_get_active_time_log")
    offices = serializers.SerializerMethodField("_get_offices")

    def _get_offices(self, instance):
        _offices = []
        for office in instance.offices.all():
            _offices.append(OfficeSerializer(office).data)
        return _offices

    def _get_active_time_log(self, instance):
        try:
            timelog = TimeLog.objects.order_by("-id").first()
            if not timelog.time_out:
                return TimeLogSerializer(timelog).data
        except:
            pass
        return None
     
    class Meta:
        fields = ["id", "employee_id", "first_name", "last_name", "active_time_log", "offices"]
        model = User
