from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.TextField()
    book_url = models.TextField()
    cover_image = models.TextField()
    author = models.TextField()
    title = models.TextField()
    price = models.TextField()
    description = models.TextField()
    publisher = models.TextField()
    published_date = models.TextField()
    number_of_pages = models.TextField()
    genre = models.TextField()
    
    def __str__(self):
        return f"{self.title} - {self.author}"