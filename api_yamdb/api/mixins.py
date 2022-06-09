from rest_framework import mixins, viewsets
from rest_framework import filters
from .permissions import (
    IsAdmin,
    ReadOnly,
)


class CreateListDestroyMixin(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    permission_classes = [IsAdmin | ReadOnly]
    lookup_field = 'slug'
