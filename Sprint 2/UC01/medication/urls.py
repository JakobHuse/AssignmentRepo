from django.urls import path

from .views import medication_home_view, add_medication, medication_detail, update, delete

app_name = "medication"

urlpatterns = [
    path("", medication_home_view, name="home"),
    path("add/", add_medication, name="add"),
    path("<int:id>/", medication_detail, name="detail"),
    path("<int:id>/update/", update, name="update"),
    path("<int:id>/delete/", delete, name="delete"),
]