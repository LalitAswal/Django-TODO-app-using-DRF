"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiOverview, name = 'api-overview' ),
    path('task-list/', views.taskList, name = 'api-list' ),
    path('create-task/', views.createTask, name = 'create-task' ),
    path('update-task/<str:pk>', views.updateTask, name = 'update-task' ),
    path('delete-task/<str:pk>', views.deleteTask, name = 'delete-task' ),
    path('task-Details/<str:pk>', views.taskDetails, name = 'taskDetails' ),
]
