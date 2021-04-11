from blog.api.serializers import PostSerializer
from rest_framework import (
    generics, 
    response, 
    status
    )

from blog.models import Category, Post


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
