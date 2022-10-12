from rest_framework.views import APIView
from rest_framework.response import Response
import json
from .serializers import ReviewSerializer
from book.serializers import BookSerializer
from .models import Review, Book
from book.views import BookViewset

class ReviewViewset(APIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request):
        print("book: ", request.GET.get('book_id'))
        data_book_id = request.GET.get('book_id')
        book = Book.objects.filter(book_id=data_book_id)
        if not book:
            return Response('No book exists')
        book_id = book[0].id
        reviews = Review.objects.filter(book = book_id)
        data = list(ReviewSerializer(reviews, many=True).data)
        return Response(data)

    def post(self, request, format=None):
        user_id = self.request.user
        received_json_data=json.loads(request.body)

        geekbooks_review_data = request.data["geekbooksReviewData"]

        try:
            book_id = Book.objects.get(book_id = received_json_data['id'])
        except:
            BookViewset.create_book(self, received_json_data)
            book_id = Book.objects.get(book_id = received_json_data['id'])
        
        try: 
            Review.objects.create(
                book = book_id,
                user = user_id,
                rating = int(geekbooks_review_data["rating"]),
                review_title = geekbooks_review_data["review_title"],
                review_body = geekbooks_review_data["review_body"],
            )
            response = {"Success": "Review created"}
        except:
            response = {"Error": "Review not created"}
        return Response(response)
