from django.contrib import admin
from .models import Book, Author, Award, AwardDetails

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


class AwardAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'sort_name',
        'description',
    )


class AwardDetailsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = (
        'id',
        'award',
        'book',
        'award_year',
        'category'
    )

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(AwardDetails, AwardDetailsAdmin)