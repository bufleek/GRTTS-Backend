from rest_framework import serializers

from main.models import Office

"""Serializes and Deserializes the Office Model"""
class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Office 