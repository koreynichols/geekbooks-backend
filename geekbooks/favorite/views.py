from rest_framework import viewsets
from .serializers import FavoriteSerializer
from .models import Favorite

class FavoriteViewset(viewsets.ModelViewSet):
    model = Favorite
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        user_id = 1

        user_favorites = Favorite.objects.filter(user=user_id)
        return (user_favorites)