from django import forms
from django.forms import ModelForm

from book.models import BookReview, Book, BookAuthor


class CommentForm(forms.ModelForm):
    class CommentForm(forms.ModelForm):
        stars = forms.IntegerField(max_value=5, min_value=1)
        
    class Meta:
        model = BookReview
        fields = ['stars', 'comment']
class EditCommentForm(forms.ModelForm):
    class CommentForm(forms.ModelForm):
        stars = forms.IntegerField(max_value=5, min_value=1)
    class Meta:
        model = BookReview
        fields = ['comment', 'stars']


class AddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'desk', 'isbn']


class AddAuthorForm(ModelForm):
    class Meta():
        model = BookAuthor
        fields = ['book', 'author']
