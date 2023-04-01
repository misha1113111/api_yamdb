from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title
from rest_framework.validators import UniqueValidator
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


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')
        lookup_field = 'slug'


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )

    class Meta:
        model = Title
        fields = '__all__'


class TitleListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    rating = serializers.IntegerField()

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'rating',
            'description', 'genre', 'category'
        )

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Review
        exclude = ['title']
        read_only_fields = (
            'id', 'author', 'pub_date',
        )
    def validate(self, data):
        if self.context['request'].method == 'POST':
            user = self.context['request'].user
            title_id = self.context['view'].kwargs.get('title_id')
            if Review.objects.filter(author=user, title_id=title_id).exists():
                raise serializers.ValidationError('Вы уже оставили отзыв.')
        return data

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        exclude = ['review']
        read_only_fields = (
            'id', 'author', 'pub_date',
        )