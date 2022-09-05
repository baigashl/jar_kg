from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from blog.serializers import PostSerializers
from .serializers import MyTokenObtainPairSerializer, UserListSerializer
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from .permissions import AnonPermissionOnly


class MyObtainPairView(TokenObtainPairView):
    permission_classes = (AnonPermissionOnly,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AnonPermissionOnly,)
    serializer_class = RegisterSerializer


class UserListApiView(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes =
    serializer_class = UserListSerializer

    def get_queryset(self):
        qs = User.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

