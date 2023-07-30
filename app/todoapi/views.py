from  .serializers import SerializerTask
from .models import Task
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response




@api_view(['GET'])
def apiOverview(request):
    api_url ={
        'List':'/task-list',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>',
    }
    return Response(api_url)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = SerializerTask(tasks, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetails(request, pk):
    task = Task.objects.get(id=pk)
    serializer = SerializerTask(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createTask(request):
    serializer = SerializerTask(data =request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateTask(request, pk):
    # task = Task.objects.get(id=pk)
    task = get_object_or_404(Task, id=pk)
    serializer = SerializerTask(instance= task, data =request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def deleteTask(request, pk):
    # task = Task.objects.get(id=pk)
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return Response('Task deleted successfully', status=status.HTTP_204_NO_CONTENT)
