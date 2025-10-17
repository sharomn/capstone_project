from django.urls import path
from django.urls import path
from .views import InteractionsHomeView, LikeCreateView, CommentCreateView

urlpatterns = [
    path('', InteractionsHomeView.as_view(), name='interactions-home'),
    path('like/', LikeCreateView.as_view(), name='like-post'),
    path('comment/', CommentCreateView.as_view(), name='comment-post'),
]