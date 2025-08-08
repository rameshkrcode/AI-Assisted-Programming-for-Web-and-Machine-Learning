
from django.db import models
from rest_framework import serializers, viewsets
from rest_framework.routers import DefaultRouter
from django.urls import path, include

# Task Model
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)

# Task Serializer
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# Task ViewSet
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# URL Routing
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
