from rest_framework import serializers

from book.models import Book, BookReview


class BookReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = ['id','user','book','comment','stars']