from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from book import views as book_views
from review import views as review_views
from favorite import views as favorite_views

router = routers.DefaultRouter()
router.register(r'book', book_views.BookViewset)
router.register(r'review', review_views.ReviewViewset)
router.register(r'favorite', favorite_views.FavoriteViewset, basename="favorites")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
