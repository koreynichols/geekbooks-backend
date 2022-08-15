from rest_framework.views import APIView
from rest_framework.response import Response
import json
from .serializers import ReviewSerializer
from book.serializers import BookSerializer
from .models import Review, Book

class ReviewViewset(APIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request):
        data_book_id = request.data['book_id']
        book = Book.objects.filter(book_id=data_book_id)
        book_id = book[0].id
        reviews = Review.objects.filter(book = book_id)
        data = list(ReviewSerializer(reviews, many=True).data)
        return Response(data)

    def post(self, request, format=None):
        # user_id = self.request.user
        print(request.data['test'])
        return Response({'it worked': "message"})
