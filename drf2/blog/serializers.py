from . models import Blog,Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        field = "__all__"
        
        
class BlogSerializer(serializers.ModelSerializer):
    # realted name of comment is same as used below and comment model
    comments = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Comment
        field = "__all__"
        

        
        