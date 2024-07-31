from os import name

from django.urls import path

from api.views import BookReviewDetailAPIVIew, BookreviewListAPIView, BookDetailAPIVIew, BookListAPIView

app_name = 'api'

urlpatterns = [
    path('reviews/<int:id>/', BookReviewDetailAPIVIew.as_view(), name='review-detail'),
    path('books/<int:id>/', BookDetailAPIVIew.as_view(), name='book-detail'),
    path('reviews/', BookreviewListAPIView.as_view(), name='review-list'),
    path('books/', BookListAPIView.as_view(), name='book-list'),
]
