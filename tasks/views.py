from rest_framework import viewsets, permissions
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