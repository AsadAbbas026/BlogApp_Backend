from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveAPIView, CommentListCreateAPIView, TopPostsAPIView, MostActiveUserAPIView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='posts-list-create'),
    path('posts/<int:pk>/', PostRetrieveAPIView.as_view(), name='posts-detail'),
    path('posts/<int:post_id>/comments/', CommentListCreateAPIView.as_view(), name='comments-list-create'),
    path('top-posts/', TopPostsAPIView.as_view(), name='top-posts'),
    path('most-active-user/', MostActiveUserAPIView.as_view(), name='most-active-user'),
]