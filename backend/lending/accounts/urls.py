from django.urls import path

from .views import CustomUserCreate, BlacklistRefreshView

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name='create_user'),
    path('logout/blacklist/', BlacklistRefreshView.as_view(), name='blacklist'),
]
