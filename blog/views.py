from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from .models import User, Post, Comment
from .serializers import PostSerializer, CommentSerializer, UserSerializer

# -------------------
# Posts API
# -------------------
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# -------------------
# Comments API
# -------------------
class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(post_id=self.kwargs['post_id'])


# -------------------
# Custom Endpoints
# -------------------
@api_view(['GET'])
def top_three_posts(request):
    posts = Post.objects.annotate(comment_count=Count('comments')) \
        .order_by('-comment_count')[:3]
    data = [{"title": post.title, "num_comments": post.comment_count} for post in posts]
    return Response(data)


@api_view(['GET'])
def most_active_user(request):
    user = User.objects.annotate(total_comments=Count('comments')) \
        .order_by('-total_comments').first()
    if user:
        data = {"name": user.name, "total_comments": user.total_comments}
    else:
        data = {}
    return Response(data)