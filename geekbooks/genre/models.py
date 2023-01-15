from django.db import models

# Create your models here.

class Genre(models.Model):
    genre = models.TextField()

    def __str__(self):
        return f"{self.genre}"