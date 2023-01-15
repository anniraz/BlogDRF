from django.contrib import admin

from apps.posts.models import Post, PostImage,PostsLike

admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(PostsLike)
