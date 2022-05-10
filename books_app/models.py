from operator import length_hint
from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=150, null=True, blank=True)
    sort_name = models.CharField(max_length=150, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
  
    def get_friendly_name(self):
        return self.friendly_name


class Book(models.Model):
    author = models.ForeignKey('Author', null=True, blank=True, on_delete=models.SET_NULL)
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=256)
    sort_title = models.CharField(max_length=256)
    year = models.PositiveIntegerField()
    pages = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rating_count = models.PositiveIntegerField()
    plot = models.TextField()
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
