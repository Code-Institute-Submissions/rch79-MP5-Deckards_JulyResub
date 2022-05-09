from django.contrib import admin
from .models import Book, Author

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = (
        'isbn',
        'title',
        'author',
        'price',
        'rating',
        'image'
    )

    ordering = ('sort_title', )


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)