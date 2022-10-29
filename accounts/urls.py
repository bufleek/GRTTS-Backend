from django.urls import path

from accounts import views

urlpatterns = [
    path("auth/", views.Authenticate.as_view()),
    path("token/refresh/", views.RefreshToken.as_view()),
    path("token/verify/", views.VerifyToken.as_view()),
]
