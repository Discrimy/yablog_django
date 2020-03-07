from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ShortedUrl(models.Model):
    original_url = models.CharField('Original URL', max_length=512)
    redirects = models.IntegerField('Redirects', default=0)
    created_at = models.DateTimeField('Created At')

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
