from rest_framework import serializers
from .models import HomeBookList

class HomeBookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeBookList
        fields = "__all__"
        depth = 1