from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from accounts.models import User
from accounts.serializers import ObtainTokenSerializer, UserSerializer


# Create your views here.
class Authenticate(TokenObtainPairView):
    serializer_class = ObtainTokenSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if(response.status_code == 200):
            try:
                user = User.objects.get(username=request.data.get("username"))
                response.data["user"] = UserSerializer(user).data
            except:
                pass
        return response

class RefreshToken(TokenRefreshView):
    permission_classes = [AllowAny]

class VerifyToken(TokenVerifyView):
    permission_classes = [AllowAny]
