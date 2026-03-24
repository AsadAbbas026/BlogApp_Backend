from django.urls import path
from .views import (
    PostListCreateView, PostDetailView, CommentListCreateView,
    top_three_posts, most_active_user
)

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='post-comments'),
    path('top-posts/', top_three_posts, name='top-three-posts'),
    path('most-active-user/', most_active_user, name='most-active-user'),
]