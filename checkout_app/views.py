from django.shortcuts import redirect, render, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Your shopping bag is empty!')
        return redirect(reverse('books'))

    order_form = OrderForm()
    template = 'checkout_app/checkout.html'
    context = {
        'order_form': order_form
    }

    return render(request, template, context)
