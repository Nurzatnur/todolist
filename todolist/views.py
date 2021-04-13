from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from todolist.serializers import *
from todolist.models import Task


@api_view(['GET'])
def taskOverview(request):
    todo_urls = {
        'List' : '/task-list/',
        'Detail View' : '/task-detail/<int:pk>',
        'Create' : '/task-create/',
        'Update' : '/task-update/<int:pk>',
        'Delete' : '/task-delete/<int:pk>',
    }
    return Response(todo_urls)

class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all().order_by()

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer

class TaskUpdateView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class TaskDeleteView(generics.DestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

