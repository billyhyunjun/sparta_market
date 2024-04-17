from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Card(models.Model):
    cardnum = models.TextField()

    def __str__(self):
        return self.cardnum
    
class User(AbstractUser):
    point = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images/", blank=True)
    following = models.ManyToManyField('self',symmetrical=False, related_name="followers")
    cards = models.ManyToManyField(Card, blank=True, related_name="card_users")