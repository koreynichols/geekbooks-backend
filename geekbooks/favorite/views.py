from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from .serializers import FavoriteSerializer
from .models import Favorite
import json
from .models import Book
from book.views import BookViewset
from book.serializers import BookSerializer

class FavoriteViewset(APIView):

    model = Favorite
    serializer_class = FavoriteSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        print(self.request)
        user_id = self.request.user.id

        user_favorites = Favorite.objects.filter(user=user_id)
        user_favorites = user_favorites.filter(is_favorite=True)
        try:
            user_favorites = user_favorites.filter(book__book_id = request.data["book_id"])
        except:
            print("No book ID")
        data = list(FavoriteSerializer(user_favorites, many=True).data)

        print(data)

        return Response(data)


    def post(self, request, format=None):

        user_id = self.request.user
        received_json_data=json.loads(request.body)
        received_json_data=received_json_data["book"]

        try:
            book_id = Book.objects.get(book_id = received_json_data['id'])
        except:
            BookViewset.create_book(self, received_json_data)
            book_id = Book.objects.get(book_id = received_json_data['id'])


        try:
            favorite = Favorite.objects.get(user=user_id, book = book_id)
            favorite.is_favorite = not favorite.is_favorite;
            favorite.save()
            response = {'message' : 'Book Favorite Changed'}
        except:
            Favorite.objects.create(book = book_id, user = user_id, is_favorite = 'True')
            response = {'message': 'Book Favorite created'}
        response={'test': 'it worked'}
        return Response(response, status=status.HTTP_200_OK)