from django.urls import path
from .views import (
     TaskListView,
     TaskCreateView,
     TaskToggleView,
     TaskDeleteView,
)

urlpatterns = [
    path('',                 TaskListView.as_view(),   name = 'task_list'),
    path('create/',          TaskCreateView.as_view(), name = 'task_create'),
    path('toggle/<int:pk>/', TaskToggleView.as_view(), name = 'task_toggle'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name = 'task_delete'),
]