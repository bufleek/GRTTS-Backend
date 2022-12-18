from rest_framework import serializers

from main.models import Office, TimeLog

"""Serializes and Deserializes the Office Model"""
class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Office 

"""Serializes and Deserializes the TimeLog Model"""
class TimeLogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = TimeLog