from rest_framework import viewsets, permissions,status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing task instances.
    This one class handles:
    - GET /api/tasks/ (List)
    - POST /api/tasks/ (Create)
    - GET /api/tasks/<id>/ (Retrieve)
    - PUT/PATCH /api/tasks/<id>/ (Update)
    - DELETE /api/tasks/<id>/ (Delete)
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        # Return tasks only for the authenticated user
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        #create a nw task and automatically set the user
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def toggle(self, request, pk=None):
        """
        Custom action to toggle the completion status of a task.
        URL: POST /api/tasks/{id}/toggle/
        """
        task = self.get_object() #safly gets the task usin our permissions
        task.is_completed = not task.is_completed #Flip the True/False value
        task.save()

        #we return the updated task data so the frontend can refresh
        serializer = self.get_serializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)