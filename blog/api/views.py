from blog.api.serializers import PostSerializer
from rest_framework import (
    generics, 
    response, 
    status
    )

from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, BasePermission, SAFE_METHODS

from blog.models import Category, Post

class PostUserWritePermission(BasePermission):
    message = 'Editing post is restricted to author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class PostList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
