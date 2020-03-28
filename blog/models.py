from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField('Title', max_length=128)
    content = models.TextField('Content')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    content = models.TextField('Content')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
