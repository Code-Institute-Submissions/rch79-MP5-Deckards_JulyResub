from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from django.conf import settings

import stripe

from bag_app.contexts import bag_contents
from .forms import OrderForm

# Create your views here.


def checkout(request):

    # retrieve bag contents or display error msg if bag empty
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Your shopping bag is empty!')
        return redirect(reverse('books'))
    current_bag = bag_contents(request)

    order_form = OrderForm()
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    total = current_bag['grand_total']
    stripe_total = round(total *100)

    # create payment intent based on bag grand total and default currency
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    # check if stripe public key environment variable has been setup
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key not found. \
            Please add it to environment variables')

    template = 'checkout_app/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
