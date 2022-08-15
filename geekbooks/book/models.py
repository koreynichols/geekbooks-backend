from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.TextField()
    book_url = models.TextField()
    cover_image = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    published_date = models.TextField(blank=True, null=True)
    number_of_pages = models.TextField(blank=True, null=True)
    genre = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.author}"