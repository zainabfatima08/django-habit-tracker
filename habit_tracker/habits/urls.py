from django.urls import path
from .views import (
     HabitListView,
     HabitCreateView,
     ToggleHabitView,
     HabitDetailView,
)

urlpatterns = [
    path("",                 HabitListView.as_view(),                   name = "habit_list"),
    path("create/",          HabitCreateView.as_view(),          name = "habit_create"),
    path("toggle/<int:pk>/", ToggleHabitView.as_view(), name = "toggle_habit"),
    path("<int:pk>/",        HabitDetailView.as_view(),        name = "habit_detail")
]