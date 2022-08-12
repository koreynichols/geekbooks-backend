# from rest_framework import viewsets, status
# from .serializers import FavoriteSerializer
# from .models import Favorite
# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.decorators import action



# class FavoriteViewset(generics.ListCreateAPIView):
#     model = Favorite
#     serializer_class = FavoriteSerializer

#     @action(detail=True, methods=['POST'])
#     def set_favorite(self, request):
#         # return Response("ok")
#         user_id = self.request.user
#         book_id = request.book

#         try:
#             favorite = Favorite.objects.get(user=user_id, book = book_id)
#             favorite.delete();
#             response = {'message' : 'Book Favorite deleted'}
#         except:
#             Favorite.objects.create(book = book_id, user = user_id, is_favorite = 'true')
#             response = {'message': 'Book Favorite created'}
#         return Response(response, status=status.HTTP_200_OK)


#     # def get_queryset(self):
#     #     user_id = self.request.user

#     #     user_favorites = Favorite.objects.filter(user=user_id)
#     #     return (user_favorites)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from .serializers import FavoriteSerializer
from .models import Favorite
import json
from .models import Book

class FavoriteViewset(APIView):

    model = Favorite
    serializer_class = FavoriteSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        user_id = self.request.user

        user_favorites = Favorite.objects.filter(user=user_id)
        data = list(FavoriteSerializer(user_favorites, many=True).data)

        return Response(data)


    def post(self, request, format=None):
        user_id = self.request.user
        book_id = Book.objects.get(id = request.POST.get('book'))

        try:
            favorite = Favorite.objects.get(user=user_id, book = book_id)
            favorite.delete();
            response = {'message' : 'Book Favorite deleted'}
        except:
            Favorite.objects.create(book = book_id, user = user_id, is_favorite = 'True')
            response = {'message': 'Book Favorite created'}
        return Response(response, status=status.HTTP_200_OK)