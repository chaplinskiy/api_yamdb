from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken


from .permissions import (
    IsAdminOrReadOnly,
    IsAdminRole,
    IsStaffOrOwnerOrReadOnly,
)

from .serializers import (
    CategorySerializer,
    CommentSerializer,
    ConfirmationSerializer,
    EmailSerializer,
    GenreSerializer,
    ReviewSerializer,
    TitleSerializer,
    UserForAdminSerializer,
    UserSerializer,
)

from reviews.models import Category, Comment, Genre, Title, Review


User = get_user_model()


@api_view(['POST'])
def signup(request):
    serializer_data = EmailSerializer(data=request.data)
    serializer_data.is_valid(raise_exception=True)
    email = serializer_data.data.get('email')
    username = serializer_data.data.get('username')
    if username == 'me':
        return Response('неверное имя пользователя',
                        status=status.HTTP_400_BAD_REQUEST)
    user, create = User.objects.get_or_create(email=email, username=username,
                                              is_active=False)
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        'Код проверки почты',
        f'Ваш код подтверждения: {confirmation_code}',
        settings.DEFAULT_FROM_EMAIL, [email])
    return Response({'email': email, 'username': username})


@api_view(['POST'])
def get_token(request):
    serializer_data = ConfirmationSerializer(data=request.data)
    serializer_data.is_valid(raise_exception=True)
    confirmation_code = serializer_data.data.get('confirmation_code')
    username = serializer_data.data.get('username')
    user = get_object_or_404(User, username=username)
    if default_token_generator.check_token(user, confirmation_code):
        user.is_active = True
        user.save()
        token = AccessToken.for_user(user)
        return Response({'token': f'{token}'}, status=status.HTTP_200_OK)
    return Response('Неверный код подтверждения',
                    status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserForAdminSerializer
    permission_classes = [IsAdminRole]
    lookup_field = 'username'
    filter_backends = [filters.SearchFilter]
    search_fields = [
        '=username',
    ]

    @action(
        methods=['get', 'patch'],
        detail=False,
        permission_classes=[IsAuthenticated],
    )
    def me(self, request):
        serializer = UserSerializer(request.user)
        if request.method == 'PATCH':
            serializer = UserSerializer(
                request.user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'


class CommentViewSet(viewsets.ModelViewSet):
    # queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsStaffOrOwnerOrReadOnly,)

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return serializer.save(author=self.request.user, review=review)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsStaffOrOwnerOrReadOnly,)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return serializer.save(author=self.request.user, title=title)


class TitleViewSet(viewsets.ModelViewSet):
    # queryset = Title.objects.all()
    # def get_queryset(self):
    #     return Title.objects.all().annotate(rating=Avg('reviews__score'))
    queryset = Title.objects.all().annotate(rating=Avg('reviews__score'))
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    # pagination_class =
    # lookup_field = 'username'
    # filter_backends = [filters.SearchFilter]
    # search_fields = [
    #     '=username',
    # ]
