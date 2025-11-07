from django.urls import path

from .views import medication_home_view, add_medication, medication_detail #delete_medication

app_name = "medication"

urlpatterns = [
    path("", medication_home_view, name="home"),
    path("add/", add_medication, name="add"),
    path("<int:id>/", medication_detail, name="detail")
    #path("delete/", delete_medication, name="delete"),
]