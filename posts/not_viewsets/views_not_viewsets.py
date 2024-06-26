from django.contrib.auth import get_user_model

from rest_framework import generics

from .permissions import IsAuthorReadOnly
from .models import Post
from .serializers import PostSerializer, UserSerializer


class PostList(generics.ListCreateAPIView):
  permission_classes = (IsAuthorReadOnly,)
  queryset = Post.objects.all()
  serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthorReadOnly,)
  queryset = Post.objects.all()
  serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer 


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer