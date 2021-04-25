from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from blog.api.serializers import PostSerializer
from rest_framework import (
    generics, 
    response, 
    status,
    viewsets,
    mixins
    )

from rest_framework.permissions import (
    IsAdminUser, 
    DjangoModelPermissionsOrAnonReadOnly, 
    BasePermission, 
    SAFE_METHODS, 
    IsAuthenticated
    )
from rest_framework import filters
from rest_framework.response import Response

from blog.models import Category, Post
from .serializers import PostSerializer
from rest_framework.views import APIView
class PostUserWritePermission(BasePermission):
    message = 'Editing post is restricted to author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class PostList(generics.ListAPIView):
   
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)
    

class PostDetail(generics.RetrieveAPIView):
    
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # def get_queryset(self):
    #     slug = self.request.query_params.get('slug', None)
    #     print(slug)
    #     return Post.objects.filter(slug=slug)
    def get_object(self, **kwargs):
        queryset = self.get_queryset()
        item = self.kwargs.get('slug')
        return get_object_or_404(queryset, slug=item)
class PostListDetailfilter(generics.ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']

    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    # '$' Regex search.


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


# class PostList(viewsets.ModelViewSet):
#     # permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)

#     # Define Custom Queryset
#     def get_queryset(self):
#         return Post.objects.all()

class CreatePost(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AdminPostDetail(APIView):
    querySet = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, pk=None,):
        post = self.querySet.get(id=pk)
        serializer = self.serializer_class(post)

        return Response(serializer.data)


class EditPost(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def put(self, request, pk, format=None):
        post = Post.objects.get(pk=pk)
        serializer = self.serializer_class(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeletePost(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, pk, format=None):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)