from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Book, Author

# Create your views here.

def all_books(request):
    """ Displays all available books """

    books = Book.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            if sort_key == 'sort_title':
                sort_key = 'lower_sort_title'
                books = books.annotate(lower_sort_title=Lower('sort_title'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_key = f'-{sort_key}'
            
            books = books.order_by(sort_key)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search criteria")
                return redirect(reverse('books'))
            queries = Q(title__icontains=query) | Q(description__icontains=query) | Q(plot__icontains=query)
            books = books.filter(queries)
        else:
            query=""

    current_sorting = f'{sort}_{direction}'

    context = {
        'books': books,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'books_app/books.html', context)


def all_authors(request):
    """ Displays all available authors """

    authors = Author.objects.all().order_by('sort_name')

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
    books = Book.objects.filter(author__exact=author)

    context = {
        'author': author,
        'author_books': books
    }

    return render(request, 'books_app/author_detail.html', context)
