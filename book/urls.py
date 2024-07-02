
from django.urls import path
from book.views import BookListView, BookDetailView, AddCommentView, EditReviewView, DeleteReviewView, AddBookView, \
    DeleteMessageView

app_name = 'book'

urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('<int:book_id>/', BookDetailView.as_view(), name='detail'),
    path('<int:id>/add-review/', AddCommentView.as_view(), name='add-comment'),
    path('add-book/', AddBookView.as_view(), name='add-book'),
    path('<int:id>/<int:comment_id>/edit/', EditReviewView.as_view(), name='edit-comment'),
    path('<int:id>/<int:comment_id>/delete-review/', DeleteReviewView.as_view(), name='delete-comment'),
    path('<int:id>/<int:comment_id>/delete-review-message/', DeleteMessageView.as_view(), name='delete-comment-message'),

]