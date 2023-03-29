from rest_framework import serializers


class SignUpSerializer(serializers.Serializer):
    pass

class TokenSerializer(serializers.Serializer):
    pass

class UserSerializer(serializers.ModelSerializer):
    pass

class UserMeSerializer(serializers.ModelSerializer):
    pass

class ReviewSerializer(serializers.ModelSerializer):
    pass

class CommentSerializer(serializers.ModelSerializer):
    pass

class CategorySerializer(serializers.ModelSerializer):
    pass

class GenreSerializer(serializers.ModelSerializer):
    pass

class TitleSerializer(serializers.ModelSerializer):
    pass

class TitleListSerializer(serializers.ModelSerializer):
    pass