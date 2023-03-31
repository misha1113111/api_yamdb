from rest_framework import mixins, viewsets
from .serializer import (CategorySerializer,GenreSerializer)
from reviews.models import Category, Genre, Title
from django.db.models import Avg


class SignUpView():
    pass

class TokenView():
    pass

class UserViewSet():
    pass

class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class GenreViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
    rating=Avg('reviews__score')).order_by('-id')
    

class ReviewViewSet():
    pass

class CommentViewSet():
    pass