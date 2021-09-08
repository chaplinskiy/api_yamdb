from django.urls import include, path
from rest_framework.routers import DefaultRouter


from . import views

router = DefaultRouter()
router.register('users', views.UserViewSet)


urlpatterns = [
    path('auth/signup/', views.signup, name='get_tokens_for_user'),
    path(
        'auth/token/',
        views.get_token,
        name='generate_confirmation_code',
    ),
    path('', include(router.urls)),
]
