from django.http import Http404
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from blog.models import Post
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


class UserDetailAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [SessionAuthentication]
    parser_classes = [JSONParser]

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id):
        user = self.get_object(id)
        posts = Post.objects.filter(user_id=id)
        serializer = UserListSerializer(user)
        serializer2 = PostSerializers(posts, many=True)
        data = serializer.data
        data['posts'] = serializer2.data
        data['post_count'] = len(serializer2.data)
        return Response(data)


