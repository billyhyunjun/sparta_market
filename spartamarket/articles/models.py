from django.db import models
from django.conf import settings

# Create your models here.

class Hashtag(models.Model):
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True)
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles")
    hashtags = models.ManyToManyField(Hashtag, blank=True, related_name="hashtag_articles")
    
    def __str__(self) -> str:
        return self.title
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="users")
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.content
    
