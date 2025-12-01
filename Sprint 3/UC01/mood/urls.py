from django.urls import path

from .views import mood_home_view, add_mood_entry, mood_list, entry_detail

app_name = "mood"

urlpatterns = [
    path("", mood_home_view, name="home"),
    path("add/", add_mood_entry, name="add"),
    path("list/", mood_list, name="list"),
    path("<int:id>/", entry_detail, name="detail"),
]