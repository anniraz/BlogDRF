from django.db import models
from django.contrib.auth import get_user_model

from apps.posts.models import Post

User=get_user_model()


class Comment(models.Model):
    comment = models.CharField(max_length=255)
    post = models.ForeignKey(Post, related_name='post_comment', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}--{self.post.title}--{self.user.username}"

    class Meta:
        ordering = ("-create_at",)