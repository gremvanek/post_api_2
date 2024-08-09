from post.models import Comment, Post
from django.contrib import admin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date_created", "date_modified")
    search_fields = ("title", "author__login")
    list_filter = ("date_created",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "text", "post", "date_created", "date_modified")
    search_fields = ("author__login", "text", "post__title")
