from rest_framework import generics
from .models import Post, Comment, User
from .serializers import PostSerializer, CommentSerializer, UserSerializer
from django.db.models import Count

# Posts
class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Comments
class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, post_id=self.kwargs['post_id'])

# Custom endpoints
class TopPostsAPIView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.annotate(comment_count=Count('comment')).order_by('-comment_count')[:3]

class MostActiveUserAPIView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.annotate(total_comments=Count('comment')).order_by('-total_comments')[:1]