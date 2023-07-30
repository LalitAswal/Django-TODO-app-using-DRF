from rest_framework import serializers
from .models import Task

class SerializerTask(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
