from django.shortcuts import get_object_or_404
from blog.api.serializers import PostSerializer
from rest_framework import (
    generics, 
    response, 
    status,
    viewsets
    )

from rest_framework.permissions import (
    IsAdminUser, 
    DjangoModelPermissionsOrAnonReadOnly, 
    BasePermission, 
    SAFE_METHODS, 
    IsAuthenticated
    )

from rest_framework.response import Response

from blog.models import Category, Post
from .serializers import PostSerializer

class PostUserWritePermission(BasePermission):
    message = 'Editing post is restricted to author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

# class PostList(generics.ListCreateAPIView):
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    

# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.objects.all()

#     def list(self,request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)


class PostList(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)

    # Define Custom Queryset
    def get_queryset(self):
        return Post.objects.all()

