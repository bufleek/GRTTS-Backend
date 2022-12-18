from django.urls import path

from accounts import views as account_views
from main import views as main_views

urlpatterns = [
    path("auth/", account_views.Authenticate.as_view()),
    path("token/refresh/", account_views.RefreshToken.as_view()),
    path("token/verify/", account_views.VerifyToken.as_view()),
    path("employees/<int:pk>/", main_views.UserDetailView.as_view()),
]
