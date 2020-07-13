#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danil Kovalenko

import re

from django.http import Http404
from rest_framework import serializers, status
from rest_framework.response import Response

from thread.models import Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "link", "author", "created_date", "up_votes", "id"]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ["author", "created_date", "content", "id"]

    def get_corresponding_post(self):
        uri = self.context["request"].build_absolute_uri()
        post_id_re = r"^.+/posts/(\d+)/comments/?$"
        post_id_match = re.fullmatch(post_id_re, uri)

        if post_id_match is None:
            raise Http404(f"No or invalid post id")

        post_id = post_id_match.group(1)

        try:
            return Post.objects.get(id=post_id)
        except Exception as e:
            raise Http404(f"Invalid post_id `{post_id}`") from e

    def get_404(self):
        return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, validated_data):
        related_post = self.get_corresponding_post()
        data = validated_data.copy()
        data["related_post"] = related_post
        return super().create(data)
