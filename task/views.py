from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import TaskSerializer
from .models import Task
# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
 serializer_class = TaskSerializer
 queryset=Task.objects.all()

 @api_view(['DELETE'])
 def delete_completed_tasks(request):
        Task.objects.filter(completed=True).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)