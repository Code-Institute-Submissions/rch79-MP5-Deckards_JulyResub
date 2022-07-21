from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Book, Author, Award, AwardDetails
from .forms import BookForm, AuthorForm, AwardForm, AwardDetailsForm

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


def all_awards(request):
    """ Displays all available book awards """

    awards = Award.objects.all().order_by('sort_name')

    context = {
        'awards': awards,
    }

    return render(request, 'books_app/awards.html', context)


def award_detail(request, award_id):
    """ Displays award detail """

    award = get_object_or_404(Award, pk=award_id)
    award_details = AwardDetails.objects.filter(award__exact=award).order_by('award_year')

    award_years = []
    for award in award_details:
        if award.award_year not in award_years:
            award_years.append(award.award_year)
    award_years.sort()

    context = {
        'award': award,
        'award_details': award_details,
        'award_years': award_years,
    }

    return render(request, 'books_app/award_detail.html', context)


#  ---------------------------------------------- Books

def add_book(request):
    '''Add a book to the store'''

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(), 'New book successfully added'
            messages.success(request, 'New book successfully added')
            return redirect(reverse('add_book'))
        else:
            messages.error(request, 'Failed to add new book. Please ensure information provided is valid')
    else:
        form = BookForm()

    template = 'books_app/add_book.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_book(request, book_id):
    '''Edit an existing book in the store'''

    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book successfully updated')
            return redirect(reverse('book_detail', args=[book.id]))
        else:
            messages.error(request, 'Failed to update book. Please ensure information provided is valid')
    else:
        form = BookForm(instance=book)
        messages.info(request, f'You are editing { book.title }')

    template = 'books_app/edit_book.html'
    context = {
        'form': form,
        'book': book
    }

    return render(request, template, context)


def delete_book(request, book_id):
    '''Delete an existing book'''

    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    messages.success(request, 'Book deleted')
    return redirect(reverse('books'))


#  ---------------------------------------------- Authors

def author_detail(request, author_id):
    """ Displays author detail """

    author = get_object_or_404(Author, pk=author_id)
    books = Book.objects.filter(author__exact=author)

    context = {
        'author': author,
        'author_books': books
    }

    return render(request, 'books_app/author_detail.html', context)


def add_author(request):
    '''Add an author to the store'''

    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save(), 'New book successfully added'
            messages.success(request, 'New author successfully added')
            return redirect(reverse('add_author'))
        else:
            messages.error(request, 'Failed to add new author. Please ensure information provided is valid')
    else:
        form = AuthorForm()

    template = 'books_app/add_author.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def delete_author(request, author_id):
    '''Delete an existing book'''

    author = get_object_or_404(Author, pk=author_id)
    author.delete()
    messages.success(request, 'Author deleted')
    return redirect(reverse('books'))


#  ---------------------------------------------- Awards

def add_award(request):
    '''Add an award to the store'''

    if request.method == "POST":
        form = AwardForm(request.POST)
        if form.is_valid():
            form.save(), 'New award successfully added'
            messages.success(request, 'New award successfully added')
            return redirect(reverse('add_award'))
        else:
            messages.error(request, 'Failed to add new award. Please ensure information provided is valid')
    else:
        form = AwardForm()

    template = 'books_app/add_award.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def delete_award(request, award_id):
    '''Delete an existing award'''

    award = get_object_or_404(Award, pk=award_id)
    award.delete()
    messages.success(request, 'Award deleted')
    return redirect(reverse('awards'))


#  ---------------------------------------------- Award Details

def add_award_details(request):
    '''Add award details to an existing book'''

    if request.method == "POST":
        form = AwardDetailsForm(request.POST)
        if form.is_valid():
            form.save(), 'Award Details successfully added'
            messages.success(request, 'Award Details successfully added')
            return redirect(reverse('add_award_details'))
        else:
            messages.error(request, 'Failed to add award details. Please ensure information provided is valid')
    else:
        form = AwardDetailsForm()

    template = 'books_app/add_award_details.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_award_detail(request, award_detail_id):
    '''Edit an existing book in the store'''

    award_detail = get_object_or_404(AwardDetails, pk=award_detail_id)

    if request.method == 'POST':
        form = AwardDetailsForm(request.POST, instance=award_detail)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book successfully updated')
            return redirect(reverse('awards'))
        else:
            messages.error(request, 'Failed to update book. Please ensure information provided is valid')
    else:
        form = AwardDetailsForm(instance=award_detail)
        messages.info(request, f'You are editing { award_detail.book.title }')

    template = 'books_app/edit_award_detail.html'
    context = {
        'form': form,
        'award_detail': award_detail
    }

    return render(request, template, context)


def delete_award_detail(request, award_detail_id):
    '''Delete an existing book'''

    award_detail = get_object_or_404(AwardDetails, pk=award_detail_id)
    award_detail.delete()
    messages.success(request, 'Award detail deleted')
    return redirect(reverse('awards'))



