from django.shortcuts import render
from rest_framework import permissions
from .serializers import PostSerializers
from account.permissions import IsOwnerOrReadOnly
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from .models import Post


class PostListApiView(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes =
    serializer_class = PostSerializers

    def get_queryset(self):
        qs = Post.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs


class PostCreateApiView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes =
    serializer_class = PostSerializers
    queryset = Post.objects.all()


class PostDetailApiView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    # authentication_classes =
    serializer_class = PostSerializers


class PostUpdateApiView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    # authentication_classes =
    serializer_class = PostSerializers
    queryset = Post.objects.all()


class PostDeleteApiView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    # authentication_classes =
    serializer_class = PostSerializers
    queryset = Post.objects.all()


