from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='qna', null=True, blank=True)
    # img = models. Later add image
    views = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title