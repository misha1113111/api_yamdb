from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, SignUpView, TitleViewSet,
                    TokenView, UserViewSet)

router = DefaultRouter()

router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'titles', TitleViewSet, basename='title')
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews'
                r'/(?P<review_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register(r'users', UserViewSet, basename='users')

jwt_patterns = [
    path('auth/token/', TokenView.as_view()),
    path('auth/signup/', SignUpView.as_view()),
]

urlpatterns = [
    path('', include(jwt_patterns)),
    path('', include(router.urls)),
]
