from django.db import models
from book.models import Book
from genre.models import Genre

# Create your models here.

class HomeBookList(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book} - {self.genre}"