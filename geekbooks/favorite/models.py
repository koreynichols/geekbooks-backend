from django.db import models
from book.models import Book
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint

# Create your models here.
class Favorite(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    is_favorite = models.BooleanField()

    class Meta: 
        constraints = [
                    UniqueConstraint(fields=['user', 'book'], name='book_user_favorite_unique'),
        ]

    def __str__(self):
        return f"{self.user} - {self.book}"