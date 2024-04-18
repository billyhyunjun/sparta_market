from django.db import models
from django.conf import settings

# Create your models here.
class Store(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True)
    price = models.IntegerField()
    card = models.ForeignKey(settings.AUTH_CARD_MODEL, on_delete=models.CASCADE, related_name="cards")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="stores")
    
    def __str__(self) -> str:
        return self.title