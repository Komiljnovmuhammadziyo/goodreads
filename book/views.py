from urllib import request

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import View, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import BookReview
from .forms import CommentForm, AddBookForm
import book
from book.forms import CommentForm, EditCommentForm
from book.models import Book, BookReview
from user.models import CustomUser


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        context = {'books': books}

        search_query = request.GET.get('q')
        if search_query:
            books = books.filter(title__icontains=search_query)

        page_size = request.GET.get('page_size', 3)
        paginator = Paginator(books, page_size)

        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        context = {"page_obj": page_obj,}
        return render(request, 'books/list.html', context)


class BookDetailView(View):
    def get(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        comments = BookReview.objects.filter(book=book)
        comment_form = CommentForm()
        context = {
            'book': book,
            'comments': comments,
            'form':comment_form,

        }
        return render(request, 'books/detail.html', context)

class AddCommentView(LoginRequiredMixin, View):
    def get(self, request, book_id):
        book = Book.objects.get(book_id=book_id)
        comments = BookReview.objects.filter(book=book)

        context = {
            'book': book,
            'comments': comments,
        }

        return render(request, 'home.html', context)


    def post(self, request, id):
        book = Book.objects.get(id=id)
        user = request.user
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            comment = BookReview.objects.create(
                user=user,
                book=book,
                comment=comment_form.cleaned_data['comment'],
                stars = comment_form.cleaned_data['stars']
            )
            comment.save()
            return redirect('book:detail', book.id)
        return render(request, 'books/detail.html', {'form':comment_form})
class EditReviewView(View):
    def get(self, request, id, comment_id):
        comment = get_object_or_404(BookReview, id=comment_id)
        book = comment.book
        comments = BookReview.objects.filter(book=book).exclude(id=comment_id)
        if comment.user != request.user:
            messages.error(request, "You do not have permission to edit this review.")
            return redirect(reverse('book:detail', kwargs={'id': id}))

        comment_form = CommentForm(instance=comment)
        return render(request, 'crud/edit.html', {'form': comment_form, 'book': book, 'comments': comments})

    def post(self, request, id, comment_id):
        comment = get_object_or_404(BookReview, id=comment_id)

        # Check if the user is authorized to edit the comment
        if comment.user != request.user:
            messages.error(request, "You do not have permission to edit this review.")
            return redirect(reverse('book:detail', kwargs={'id': id}))

        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, "Review updated successfully.")
            return redirect(reverse('book:detail', kwargs={'book_id': id}))
        else:
            messages.error(request, "Please correct the error below.")

        return render(request, 'crud/edit.html', {'form': comment_form})


class DeleteReviewView(View):
    def get(self, request, id, comment_id):
        review = BookReview.objects.filter(id=comment_id)
        review.delete()
        return redirect(reverse('book:detail', kwargs={'book_id': id}))

class DeleteMessageView(View):
    def get(self, request, id, comment_id):
        return render(request, 'crud/delete.html', {'book_id': id, 'comment_id': comment_id})

class AddBookView( View):
    def get(self, request):
        form = AddBookForm()
        return render(request, 'books/add_book.html', {'form': form})

    def post(self, request,):
        book_form = AddBookForm(data = request.POST, files=request.FILES)
        if book_form.is_valid():
            book = book_form.save()
            book.save()
            return redirect('book:list')
        return render(request, 'books/add_book.html', {'form':book_form})

