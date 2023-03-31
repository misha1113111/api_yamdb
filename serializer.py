from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User
from users.validator import validate_username


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(
    required=True,
    max_length=150,
    validators=[validate_username,]
    )
    email = serializers.EmailField(required=True, max_length=254)


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(
    required=True,
    max_length=150,
    )
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'confirmation_code',
        )


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
    required=True,
    max_length=150,
    validators=[validate_username,
        UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role'
        )


class UserMeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
    required=True,
    max_length=150,
    validators=[validate_username,
        UniqueValidator(queryset=User.objects.all())]
    )


    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role'
        )
        read_only_fields = ('role',)
