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