from django.urls import path, include
from todolist.views import *

urlpatterns = [
    path('', taskOverview, name="task-overviw"),
    path('task-list/', TaskListView.as_view()),
    path('task-detail/<int:pk>', TaskDetailView.as_view()),
    path('task-create/', TaskCreateView.as_view()),
    path('task-update/<int:pk>', TaskUpdateView.as_view()),
    path('task-delete/<int:pk>', TaskDeleteView.as_view()),

]