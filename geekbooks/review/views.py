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
        reviews = Review.objects.filter(book = book_id).order_by('-date_created')
        print(reviews)
        data = list(ReviewSerializer(reviews, many=True).data)
        return Response(data)

    def post(self, request, format=None):
        user_id = self.request.user
        received_json_data=json.loads(request.body)

        review_data = received_json_data["review"]
        book_data = received_json_data["book"]
        try:
            book_id = Book.objects.get(book_id = book_data['id'])
        except:
            BookViewset.create_book(self, book_data)
            book_id = Book.objects.get(book_id = book_data['id'])
        
        try: 
            review = Review.objects.create(
                book = book_id,
                user = user_id,
                rating = int(review_data["rating"]),
                review_title = review_data["review_title"],
                review_body = review_data["review_body"],
            )
            serializer = ReviewSerializer(review)
            # response = {"success": "it works"}
            response = serializer.data
        except:
            response = {"Error": "Review not created"}
        return Response(response)
