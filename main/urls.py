from django.urls import path

from main import views

urlpatterns = [
    path("offices/", views.OfficeListApiView.as_view()),
]