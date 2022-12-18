from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from accounts.models import User
from accounts.serializers import UserSerializer

"""Does employee identification"""
@api_view(["POST"])
def identify_employee(request):
    employee_id = request.data.get("employee_id", None)
    if not employee_id:
        return Response(status=400, data={"employee_id": ["This field is required"]})
    try:
        user = User.objects.get(username=employee_id)
        return Response(data=UserSerializer(user).data)
    except User.DoesNotExist:
        return Response(status=400, data={"detail": ["Employee with the employee_id does not exist"]})


"""Gets the User Details"""
class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
