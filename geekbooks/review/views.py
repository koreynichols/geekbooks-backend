from rest_framework import viewsets
from .serializers import ReviewSerializer
from .models import Review

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        book_id = 1

        book_reviews = Review.objects.filter(book=book_id)
        return (book_reviews)