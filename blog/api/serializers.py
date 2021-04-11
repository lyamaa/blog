from django.db.models import fields
from blog.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'category', 'title', 'excerpt', 'content', 'slug', 'author', 'status' )


        

         
   
  
  