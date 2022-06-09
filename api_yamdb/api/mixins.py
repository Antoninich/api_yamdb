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
    pass
