# from django.db.models import base
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'categories', views.CategoryViewSet, basename='categories')
router.register(r'genres', views.GenreViewSet, basename='genres')
router.register(r'titles', views.TitleViewSet, basename='titles')
router.register(
    r'^titles/(?P<title_id>\d+)/reviews',
    views.ReviewViewSet,
    basename='reviews'
)
# router.register('reviews', views.ReviewViewSet)
router.register(
    r'^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    views.CommentViewSet,
    basename='comments'
)

# titles += reviews, +comments


urlpatterns = [
    path('auth/signup/', views.signup, name='get_tokens_for_user'),
    path(
        'auth/token/',
        views.get_token,
        name='generate_confirmation_code',
    ),
    # path('', include(router.urls)),
    path('v1/', include(router.urls)),
]
