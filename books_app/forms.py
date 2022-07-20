from django import forms
from .models import Book, Author, Award, AwardDetails


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        authors = Author.objects.all()

        # friendly_names = [(a.id, a.get_friendly_name()) for a in authors]
        sorted_names = [(a.id, a.sort_name) for a in authors]

        self.fields['author'].choices = sorted_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black-rounded-0'


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black-rounded-0'


class AwardForm(forms.ModelForm):

    class Meta:
        model = Award
        fields = '__all__'
        exclude = ('books',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black-rounded-0'


class AwardDetailsForm(forms.ModelForm):

    class Meta:
        model = AwardDetails
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black-rounded-0'
