from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Like
from .serializers import LikeSerializer
#from interactions.views import CommentNotification

class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



#class CommentNotification:
    # your logic here
    #pass





