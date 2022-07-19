from django.db import models

# Create your models here.

class Author(models.Model):

    class Meta:
        ordering = ['sort_name']

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


class Award(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=150, null=True, blank=True)
    sort_name = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    books = models.ManyToManyField(Book, through='AwardDetails')

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class AwardDetails(models.Model):
    book = models.ForeignKey('Book', null=True, blank=True, on_delete=models.CASCADE)
    award = models.ForeignKey('Award', null=True, blank=True, on_delete=models.CASCADE)
    award_year = models.PositiveIntegerField()
    category = models.CharField(max_length=256)