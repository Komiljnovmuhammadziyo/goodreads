from django.shortcuts import render
from django.views import View

from book.models import Book

def book_view(request,id):
    detail_list = Book.objects.filter(id=id)

    context = {
        'detail_list': detail_list
    }

    return render(request,'landing_page.html',context)
