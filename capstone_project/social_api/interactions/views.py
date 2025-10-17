from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Like
from .serializers import LikeSerializer
from rest_framework import generics, permissions
from interactions.models import Comment
from interactions.serializers import CommentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
#from interactions.views import CommentNotification

class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Attach the logged-in user to the comment
        serializer.save(user=self.request.user)

class InteractionsHomeView(APIView):
    def get(self, request):
        return Response({
            "message": "Welcome to the Interactions API",
            "endpoints": {
                "like": "/api/interactions/like/",
                "comment": "/api/interactions/comment/"
            }
        })



#class CommentNotification:
    # your logic here
    #pass





