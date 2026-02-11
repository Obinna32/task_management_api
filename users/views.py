from rest_framework import generics, permissions
from .serializers import UserSerializer

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]