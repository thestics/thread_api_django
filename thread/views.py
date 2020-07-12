from rest_framework import viewsets
from django.shortcuts import render

from thread.serializers import PostSerializer, CommentSerializer
from thread.models import Post, Comment


class PostViewSet(viewsets.ModelViewSet):
    """
    Endpoint to interact with posts
    """
    queryset = Post.objects.all().order_by('-created_date')
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    Endpoint to interact with comments
    """
    queryset = Comment.objects.all().order_by('-created_date')
