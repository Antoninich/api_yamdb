from rest_framework import viewsets

from api.serializers import (
    CategorySerializer, GenreSerializer, TitleSerializer)
from reviews.models import Category, Genre, Title


class CategoryViewSet(viewsets.ModelViewSet):
    """API Category"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(viewsets.ModelViewSet):
    """API Genre"""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    """API Title"""

    queryset = Title.objects.all()
    serializer_class = TitleSerializer
