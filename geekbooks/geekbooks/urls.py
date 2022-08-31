from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from rest_framework_simplejwt import views as jwt_views

from book import views as book_views
from review import views as review_views
from favorite import views as favorite_views
from api import views as api_views

router = routers.DefaultRouter()
router.register(r'book', book_views.BookViewset)

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/favorites/', favorite_views.FavoriteViewset.as_view(), name="favorite"),
    path('api/reviews/', review_views.ReviewViewset.as_view(), name="review"),
    path('google-api/', api_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include(router.urls)),
]
