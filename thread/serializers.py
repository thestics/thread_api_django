#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danil Kovalenko


from rest_framework import serializers

from thread.models import Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'link', 'author', 'created_date', 'up_votes']


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = ['author', 'created_date', 'content', 'related_post']