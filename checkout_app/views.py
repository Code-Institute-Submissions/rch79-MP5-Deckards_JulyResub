from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from django.conf import settings

from bag_app.contexts import bag_contents
from .forms import OrderForm

import stripe


# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Your shopping bag is empty!')
        return redirect(reverse('books'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total *100)
    order_form = OrderForm()
    template = 'checkout_app/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KydMFIg1o5vEikrTG58yiBJbbvZ9kyPpY53PTunOMxA7HdkFk2Ca8gl04RlUm7f80nSh0xMUDYNrgzQh9cE2zmq00ezI2r9fS',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
