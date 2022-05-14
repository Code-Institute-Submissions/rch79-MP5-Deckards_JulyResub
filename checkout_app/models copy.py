import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from books_app.models import Book

# Create your models here.


class Order(models.Model):
    '''Order details'''

    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=64, null=False, blank=False)
    email = models.EmailField(max_length=256, null=False, blank=False)
    phone_number = models.CharField(max_length=24, null=False, blank=False)
    address_line1 = models.CharField(max_length=80, null=False, blank=False)
    address_line2 = models.CharField(max_length=80, null=False, blank=False)
    town_or_city = models.CharField(max_length=24, null=False, blank=False)
    county = models.CharField(max_length=80, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    date = models.DateTimeField(auto_now=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        '''
        Generates unique order number
        '''
        return uuid.uuid4().hex.upper()

    def update_total(self):
        '''
        Update grand total each time
        new book is added to bag
        '''
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        '''
        Set order number if not already set. Overrides default save method
        '''
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)


class OrderLineItem(models.Model):
    '''Products in customer order'''

    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    book = models.ForeignKey(Book, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        '''
        Set lineitem total and update order total. Overrides default save method
        '''
        self.lineitem_total = self.book.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'ISBN {self.book.isbn} on order {self.order.order_number}'
