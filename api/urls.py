from os import name

from django.urls import path

from api.views import BookReviewDetailAPIVIew
app_name = 'api'

urlpatterns = [
    path('review-detail/<int:id>/', BookReviewDetailAPIVIew.as_view(), name='review-detail'),
]
