from posts.models import Post
from users.models import User
from interactions.models import Like, Comment
from rest_framework import serializers
from .models import Post
from interactions.serializers import CommentSerializer
 # Import these if not already

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    like_count = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'image', 'created_at', 'updated_at', 'like_count', 'comments']

    def get_like_count(self, obj):
        return obj.likes.count()

    def get_comments(self, obj):
        comments = obj.comments.all().order_by('-created_at')
        return CommentSerializer(comments, many=True).data
    

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at']


