from django.shortcuts import render
from django.views import View
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import BookReviewDetailSerializer
from book.models import BookReview


class BookReviewDetailAPIVIew(APIView):
    def get(self, request, id):
        book_review = BookReview.objects.get(id = id)
        serializer = BookReviewDetailSerializer(book_review)

        return Response(serializer.data)



class BookreviewListAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        book_reviews = BookReview.objects.all().order_by('-created_at')
        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(book_reviews, request)
        serializer = BookReviewDetailSerializer(page_obj, many=True)
        return paginator.get_paginated_response(serializer.data)


# class BookReviewDetailAPIVIew(View):
#     def get(self, request, id):
#         book_review = BookReview.objects.get(id=id)
#
#         json_data = {
#             'id':book_review.id,
#             'comment': book_review.comment,
#             'stars':book_review.stars,
#             'book':{
#                 'id':book_review.book.id,
#                 'title':book_review.book.title,
#                 'desk':book_review.book.desk,
#                 'isbn':book_review.book.isbn
#             },
#             'user':{
#                 'id':book_review.user.id,
#                 'username':book_review.user.username,
#                 'first_name':book_review.user.first_name,
#                 'last_name':book_review.user.last_name,
#                 'email':book_review.user.email,
#             }
#         }
#
         # return JsonResponse(json_data)