from django.db import models


class Post(models.Model):

    title = models.CharField(name="title", max_length=512)
    link = models.CharField(name="link", max_length=4096)
    author = models.CharField(name="author", max_length=128)
    created_date = models.DateTimeField(auto_now=True)
    up_votes = models.IntegerField(default=0)

    def upvote(self):
        self.up_votes += 1
        self.save()


class Comment(models.Model):

    author = models.CharField(name="author", max_length=128)
    created_date = models.DateTimeField(auto_now=True)
    content = models.CharField(name="content", max_length=65536)
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE)
