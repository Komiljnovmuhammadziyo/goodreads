from rest_framework import serializers

from book.models import BookReview, Book
from user.models import CustomUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'desk','isbn','image']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class BookReviewDetailSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    book_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = BookReview
        fields = ['id', 'stars', 'comment', 'book', 'user', 'user_id', 'book_id']


class BookDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    book_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Book
        fields = '__all__'