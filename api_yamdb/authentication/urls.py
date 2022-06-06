from django.urls import path

from authentication import views
from authentication.views import CreateUserViewSet

app_name = 'auth'

urlpatterns = [
    path('signup/', CreateUserViewSet.as_view({'post': 'create'}), name='create-user'),
    path('token/', views.get_token, name='get-token'),
]
