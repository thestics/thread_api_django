from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

from thread.serializers import PostSerializer, CommentSerializer
from thread.models import Post, Comment


class PostViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Endpoint to interact with posts
    """

    queryset = Post.objects.all().order_by("-created_date")
    serializer_class = PostSerializer

    @action(detail=True)
    def upvote(self, request, pk=None):
        try:
            post = self.get_object()
            post.upvote()
            return Response({"status": "success"})
        except Exception:
            return Response({"status": "fail"})


class CommentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Endpoint to interact with comments
    """

    queryset = Comment.objects.all().order_by("-created_date")
    serializer_class = CommentSerializer
