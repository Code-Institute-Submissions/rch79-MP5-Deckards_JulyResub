from django import forms
from .models import Book, Author, Award, AwardDetails


class BookForm(fotms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        books = Book.objects.all()

        for field_name, field in self.field.items():
            field.widget.attrs['class'] = 'border-black-rounded-0'