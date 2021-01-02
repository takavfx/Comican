from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.db.models import fields

from .models import Page, Book, Author, Series


class AddBookForm(forms.ModelForm):
    book_file = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'custom-file-input',
                'placeholder': 'Choose files...',
                'id': 'book_file'
            }
        )
    )
    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field == forms.fields.ImageField:
                field.widget.attrs["class"] = "custom-file-input"
            else:
                field.widget.attrs["class"] = "form-control"


class AddPageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field == forms.fields.ImageField:
                field.widget.attrs["class"] = "custom-file-input"
                field.widget.attrs["placeholder"] = "Choose files..."
            else:
                field.widget.attrs["class"] = "form-control"


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class UserCreationForm(UserCreationForm):
    """
    docstring
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = ("username", "password1", "password2",)
        