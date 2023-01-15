from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HomeBookListSerializer
from .models import HomeBookList

class HomeBookListViewSet(APIView):
    model = HomeBookList
    serializer_class = HomeBookListSerializer

    def get(self, request, format=None):

        genre = request.GET.get("genre")
        books = HomeBookList.objects.filter(genre=genre)

        data = list(HomeBookListSerializer(books, many=True).data)
        return Response(data)