from rest_framework import mixins, viewsets, generics
from .serializers import (CategorySerializer,GenreSerializer,
                          ReviewSerializer,CommentSerializer, 
                          SignUpSerializer, UserSerializer, 
                          TokenSerializer)
from reviews.models import Category, Genre, Title
from django.db.models import Avg
from users.models import User


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer

class TokenView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = TokenSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
    serializer_class = ReviewSerializer
    

class CommentViewSet():
    serializer_class = CommentSerializer
    