from dataclasses import fields
from rest_framework import serializers
from .models import NewPost, Comments, Like





class CommentsSerializer(serializers.ModelSerializer):
    class Meta :
        model = Comments
        # fields = '__all__'
        fields  = [
           "comment",
           "create",
        
        ]


class LikeSerializer(serializers.ModelSerializer):
    class Meta :
        model = Like        
        fields = '__all__'

class NewPostSerializer(serializers.ModelSerializer):
    
    comments = CommentsSerializer(many=True, )
    likes = LikeSerializer(many=True)

    class Meta :
        model = NewPost
        # field = '__all__'
        fields =[
           "title",
           "content",
           "post_image",
           "created",
           "user",
           "post_view",
           "post_like",
           "comment_number",

           "comments",
           "likes"
        ]       