from django.db import models
from .validators import validate_prohibited_words
from users.models import CustomUser


class Post(models.Model):
    title = models.CharField(max_length=255, validators=[validate_prohibited_words])
    text = models.TextField()
    image = models.ImageField(upload_to="post_images/", blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:20]
