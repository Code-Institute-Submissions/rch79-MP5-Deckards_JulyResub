from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from books_app.models import Book

# Create your views here.


def view_bag(request):
    ''' Returns the shopping bag contents page'''

    return render(request, 'bag_app/shopping_bag.html')


def add_to_bag(request, book_id):
    '''Add selected qty of specified product to shopping bag'''

    book = Book.objects.get(pk=book_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # stores contents of shoppping bag in http session
    # creates a new bag if one does not currently exists
    # othewise adds to existing bag
    bag = request.session.get('bag', {})

    if book_id in list(bag.keys()):
        bag[book_id] += quantity
    else:
        bag[book_id] = quantity

    messages.success(request, f'Added {book.title} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, book_id):
    '''Add selected qty of specified product to shopping bag'''

    book = Book.objects.get(pk=book_id)
    quantity = int(request.POST.get('quantity'))

    # stores contents of shopping bag in http session
    # creates a new bag if one does not currently exists
    # othewise adds to existing bag
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[book_id] = quantity  # changes the item qty accordingly
        messages.success(request, 'Shopping bag successfully updated')
    else:
        bag.pop(book_id)  # deletes the item if qty is set to 0
        messages.success(request, f'{book.title} removed from your bag')

    request.session['bag'] = bag

    # reverse returns URL in string format based on the URL name in urls.py
    return redirect(reverse(view_bag))


def remove_from_bag(request, book_id):
    ''' Removes an item from the bag'''

    book = Book.objects.get(pk=book_id)

    try:

        bag = request.session.get('bag', {})
        bag.pop(book_id)

        request.session['bag'] = bag
        messages.success(request, f'{book.title} removed from your bag')
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def clear_bag(request):
    '''Clears all items from shopping bag'''
    bag = request.session.get('bag', {})
    bag.clear()
    request.session['bag'] = bag
    messages.success(request, 'Shopping bag successfully cleared')
    return redirect(reverse(view_bag))
