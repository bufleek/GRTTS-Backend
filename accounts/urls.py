from django.urls import path

from accounts import views as account_views

urlpatterns = [
    path("auth/", account_views.identify_employee),
    path("employees/<int:pk>/", account_views.UserDetailView.as_view()),
]
