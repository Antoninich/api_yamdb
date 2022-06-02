from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import CategoryViewSet, GenreViewSet, TitleViewSet, ReviewViewSet, CommentViewSet

API_VERSION_V1 = 'v1'

router_v1 = DefaultRouter()
router_v1.register('categories', CategoryViewSet)
router_v1.register('genres', GenreViewSet)
router_v1.register('titles', TitleViewSet)
router_v1.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet)
router_v1.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path(f'{API_VERSION_V1}/', include(router_v1.urls)),
]
