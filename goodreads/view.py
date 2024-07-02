from django.shortcuts import render
from django.views import View

from book.models import Book, BookReview


class landing_page(View):
    def get(self, request):

        return render(request, template_name='landing_page.html')

class home_page(View):
        def get(self, request):
            # book = Book.objects.get(book_id=book_id)
            comments = BookReview.objects.all()

            context = {
                # 'book': book,
                'comments': comments,
            }

            return render(request, 'home.html', context)
