from django.db.models import fields
from blog.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = ('id', 'category', 'title', 'image', 'excerpt', 'content', 'author', 'slug', 'status' )


        

         
   
  
  