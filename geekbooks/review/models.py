from django.db import models
from django.db.models import UniqueConstraint
from book.models import Book
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    rating = models.IntegerField()
    review_title = models.TextField()
    review_body = models.TextField()

    class Meta: 
        constraints = [
                    UniqueConstraint(fields=['user', 'book'], name='book_user_unique'),
        ]

    def __str__(self):
        return f"{self.user} - {self.book} - {self.rating}"