from django.urls import path

from main import views

urlpatterns = [
    path("offices/", views.get_employee_offices),
]