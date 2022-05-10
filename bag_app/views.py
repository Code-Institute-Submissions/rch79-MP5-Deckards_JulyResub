from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    ''' Returns the shopping bag contents page'''

    return render(request, 'bag_app/shopping_bag.html')


def add_to_bag(request, book_id):
    '''Add selected qty of specified product to shopping bag'''

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

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
