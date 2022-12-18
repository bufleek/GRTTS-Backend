from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from accounts.models import User
from accounts.serializers import UserSerializer
from main.models import Office
from main.serializers import OfficeSerializer

"""
Gets employee offices
"""
@api_view(["GET"])
def get_employee_offices(request):
    employee_id = request.data.get("employee_id", None)
    if not employee_id:
        return Response(status=400, data={"employee_id": ["This field is required"]})
    try:
        user = User.objects.get(username=employee_id)
        offices = []
        for office in user.offices.all():
            offices.append(OfficeSerializer(office).data)
        return Response(data=offices)
    except User.DoesNotExist:
        return Response(status=400,data={"detail": "Employee with that id does not exist"})

@api_view(["POST"])
def check_in(request):
    return Response() 