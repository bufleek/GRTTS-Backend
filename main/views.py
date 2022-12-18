import datetime

from django.utils import timezone
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import User
from main.models import TimeLog
from main.serializers import OfficeSerializer, TimeLogSerializer

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
    employee_id = request.data.get("employee_id", None)
    if not employee_id:
        return Response(status=400, data={"employee_id": ["This field is required"]})
    try:
        user = User.objects.get(username=employee_id)
        last_log = TimeLog.objects.filter(user=user).order_by('-id').first()
        if last_log and not last_log.time_out:
            return Response(status=400,data={"detail": "Employee is already checked in"})
        time_log = TimeLog.objects.create(user=user)
        return Response(data={**TimeLogSerializer(time_log).data})
    except User.DoesNotExist:
        return Response(status=400,data={"detail": "Employee with that id does not exist"})

@api_view(["POST"])
def check_out(request):
    employee_id = request.data.get("employee_id", None)
    if not employee_id:
        return Response(status=400, data={"employee_id": ["This field is required"]})
    try:
        user = User.objects.get(username=employee_id)
        last_log = TimeLog.objects.filter(user=user).order_by('-id').first()
        if last_log and last_log.time_out:
            return Response(status=400,data={"detail": "Employee is already checked out"})
        last_log.time_out = timezone.now()
        last_log.save()
        return Response(data={**TimeLogSerializer(last_log).data})
    except User.DoesNotExist:
        return Response(status=400,data={"detail": "Employee with that id does not exist"})
 

@api_view(["GET"])
def get_time_reports(request):
    employee_id = request.data.get("employee_id", None)
    if not employee_id:
        return Response(status=400, data={"employee_id": ["This field is required"]})
    try:
        user = User.objects.get(username=employee_id)
        time_reports = []
        for report in TimeLog.objects.filter(user=user).order_by("-id").all():
            time_reports.append(TimeLogSerializer(report).data)
        return Response(data=time_reports)
    except User.DoesNotExist:
        return Response(status=400,data={"detail": "Employee with that id does not exist"})
 