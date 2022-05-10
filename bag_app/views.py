from django.shortcuts import render

# Create your views here.


def view_bag(request):
    ''' Returns the shopping bag contents page'''

    return render(request, 'bag_app/shopping_bag.html')
