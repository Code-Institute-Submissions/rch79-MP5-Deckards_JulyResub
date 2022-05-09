from django.shortcuts import render
from .models import Book

# Create your views here.

def all_books(request):
    """ Displays all available books """

    books = Book.objects.all()

    context = {
        'books': books
    }

    return render(request, 'books_app/index.html', context)
