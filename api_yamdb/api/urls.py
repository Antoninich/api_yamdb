from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    CommentViewSet,
    GenreViewSet,
    ReviewViewSet,
    TitleViewSet,
    UserViewSet,
    UserMeViewSet,
)

app_name = 'api'
API_VERSION_V1 = 'v1'

router_v1 = DefaultRouter()
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(r'users', UserViewSet, basename='users')
router_v1.register(r'users/me', UserMeViewSet, basename='user-me')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path(f'{API_VERSION_V1}/', include(router_v1.urls)),
    # path(f'{API_VERSION_V1}/auth/', include('authentifications.urls')),
]
