from django.urls import path

from .views import medication_home_view

app_name = "medication"

urlpatterns = [
    path("", medication_home_view, name="home"),
]