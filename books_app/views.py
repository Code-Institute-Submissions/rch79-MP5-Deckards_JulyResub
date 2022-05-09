from django.shortcuts import get_object_or_404, render
from .models import Book

# Create your views here.

def all_books(request):
    """ Displays all available books """

    books = Book.objects.all()

    context = {
        'books': books
    }

    return render(request, 'books_app/books.html', context)


def book_detail(request, book_id):
    """ Displays book detail """

    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book
    }

    return render(request, 'books_app/book_detail.html', context)
