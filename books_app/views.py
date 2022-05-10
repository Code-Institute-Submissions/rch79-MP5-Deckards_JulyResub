from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Book, Author

# Create your views here.

def all_books(request):
    """ Displays all available books """

    books = Book.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search criteria")
                return redirect(reverse('books'))

        queries = Q(title__icontains=query) | Q(description__icontains=query) | Q(plot__icontains=query)
        books = books.filter(queries)

    context = {
        'books': books,
        'search_term': query,
    }

    return render(request, 'books_app/books.html', context)


def all_authors(request):
    """ Displays all available authors """

    authors = Author.objects.all()

    context = {
        'authors': authors,
    }

    return render(request, 'books_app/authors.html', context)
 

def book_detail(request, book_id):
    """ Displays book detail """

    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book
    }

    return render(request, 'books_app/book_detail.html', context)


def author_detail(request, author_id):
    """ Displays book detail """

    author = get_object_or_404(Author, pk=author_id)

    context = {
        'author': author
    }

    return render(request, 'books_app/author_detail.html', context)
