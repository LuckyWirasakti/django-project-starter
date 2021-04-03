from app.users.serializers import ChangePasswordSerializer, ProfileSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
# Create your views here.
class RegisterView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user