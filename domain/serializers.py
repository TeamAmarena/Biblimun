from datetime import datetime

from rest_framework import serializers

from .models import Author, User, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = []

    def validate_birth_date(self, birth_date: datetime):
        if birth_date > datetime.now():
            return serializers.ValidationError("Birth date should be set in the past")
        return birth_date


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = []


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = []
