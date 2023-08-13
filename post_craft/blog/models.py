from django.db import models
from accounts.models import User

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    postTitle = models.CharField(max_length=200, blank=False)
    postDescription = models.CharField(max_length=300, blank=False)
    postBlog = models.TextField(blank=False)
    is_saved = models.BooleanField(default=False)
    is_Published = models.BooleanField(default=False)