from django.urls import path

from main import views

urlpatterns = [
    path("offices/", views.get_employee_offices),
    path("check_in/", views.check_in),
    path("check_out/", views.check_out)
]