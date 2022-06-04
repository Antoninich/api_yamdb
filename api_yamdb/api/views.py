from rest_framework import mixins, viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from django.shortcuts import get_object_or_404

from .permissions import (
    IsAdmin,
    ReadOnly,
    ReadOnlyOrAuthorModeratorAdmin,
)
from .serializers import (
    CategorySerializer,
    GenreSerializer,
    ReviewSerializer,
    CommentSerializer,
    TitleCreateSerializer,
    TitleSerializer,
    UserSerializer,
)
from core.views import ExcludePutModelViewSet
from reviews.models import Category, Genre, Review, Title, Comment
from users.models import UserProfile


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    permission_classes = [IsAdmin | ReadOnly]


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    permission_classes = [IsAdmin | ReadOnly]


class TitleViewSet(ExcludePutModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsAdmin | ReadOnly]

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PATCH',):
            return TitleCreateSerializer
        return TitleSerializer


class ReviewViewSet(ExcludePutModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReadOnlyOrAuthorModeratorAdmin]

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs['title_id'])
        return Review.objects.filter(title=title)

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs['title_id'])
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(ExcludePutModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [ReadOnlyOrAuthorModeratorAdmin]

    def get_queryset(self):
        get_object_or_404(Title, pk=self.kwargs['title_id'])
        review = get_object_or_404(Review, pk=self.kwargs['review_id'])
        return Comment.objects.filter(review=review)

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs['review_id'])
        serializer.save(author=self.request.user, review=review)


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]
    search_fields = '=user__username'


class UserMeViewSet(mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):

    def filter_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)
