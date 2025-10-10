from django.urls import path
from .views import UserListCreateView
from .views import RegisterView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('register/', RegisterView.as_view(), name='register'),
]