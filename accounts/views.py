from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from accounts.models import User
from accounts.serializers import UserSerializer

"""Does employee identification"""
class Authenticate(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        employee_id = request.data.get("employee_id", None)
        if not employee_id:
            return Response(status=400, data={"employee_id": ["This field is required"]})
        try:
            user = User.objects.get(username=employee_id)
            return Response(data=UserSerializer(user).data)
        except User.DoesNotExist:
            return Response(status=400, data={"detail": ["Employee with the employee_id does not exist"]})

class RefreshToken(TokenRefreshView):
    permission_classes = [AllowAny]

class VerifyToken(TokenVerifyView):
    permission_classes = [AllowAny]
