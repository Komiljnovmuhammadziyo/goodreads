from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import BookReviewDetailSerializer, BookDetailSerializer
from book.models import BookReview, Book


class BookReviewDetailAPIVIew(APIView):
    def get(self, request, id):
        book_review = BookReview.objects.get(id = id)
        serializer = BookReviewDetailSerializer(book_review)

        return Response(serializer.data)

    def delete(self, request, id):
        book_review = BookReview.objects.get(id=id)
        book_review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        book_review = BookReview.objects.get(id=id)
        serializer = BookReviewDetailSerializer(instance=book_review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        book_review = BookReview.objects.get(id=id)
        serializer = BookReviewDetailSerializer(instance=book_review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookreviewListAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        book_reviews = BookReview.objects.all().order_by('-created_at')

        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(book_reviews, request)

        serializer = BookReviewDetailSerializer(page_obj, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post (self, request):
        serializer = BookReviewDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

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



class BookDetailAPIVIew(APIView):
    def get(self, request, id):
        book = Book.objects.get(id = id)
        serializer = BookDetailSerializer(book)

        return Response(serializer.data)

    def delete(self, request, id):
        book = Book.objects.get(id=id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        book = Book.objects.get(id=id)
        serializer = BookDetailSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        book = Book.objects.get(id=id)
        serializer = BookDetailSerializer(instance=book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookListAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        book = Book.objects.all().order_by('-created_at')

        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(book, request)

        serializer = BookDetailSerializer(page_obj, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post (self, request):
        serializer = BookDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
