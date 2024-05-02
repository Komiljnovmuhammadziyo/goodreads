from django.contrib import admin

from book.models import Book, Author, BookAuthor, BookReview


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn']
    search_fields = ['title', 'isbn']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']


class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ['book', 'author']


class BookReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'stars']
    list_filter = ['stars']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(BookReview, BookReviewAdmin)
