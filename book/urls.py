
from django.urls import path
from book.views import BookListView, BookDetailView

app_name = 'book'
urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('<int:book_id>/', BookDetailView.as_view(), name='detail'),
]