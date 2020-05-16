from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField('Title', max_length=128)
    content = models.TextField('Content')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField('Created At', auto_now=True)

    def __str__(self):
        return f'{self.author.username} - {self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    content = models.TextField('Content')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField('Created At', auto_now=True)

    def __str__(self):
        return f'{self.post.title} - Comment by {self.author.username}'
