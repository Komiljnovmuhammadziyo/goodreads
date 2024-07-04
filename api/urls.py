from os import name

from django.urls import path

from api.views import BookReviewDetailAPIVIew

urlpatterns = [
    path('review-detail/<int:id>/', BookReviewDetailAPIVIew.as_view(), name='review-detail'),
]
