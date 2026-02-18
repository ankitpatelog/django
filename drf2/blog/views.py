from django.shortcuts import render
from rest_framework import generics
from . models import Blog,Comment
from . serializers import BlogSerializer,CommentSerializer

# Create your views here.

class BlogView(generics.ListCreateAPIView):
    queryset = Blog.object.all()
    serializer_class = BlogSerializer(queryset)
    
class commentView(generics.ListCreateAPIView):
    queryset = Comment.object.all()
    serializer_class = CommentSerializer(queryset)
    

