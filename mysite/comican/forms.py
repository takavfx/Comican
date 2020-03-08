from django import forms

from .models import Page, Book, Auther

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class AddBookForm(forms.ModelForm):
    name = forms.CharField(label='Name',
                        max_length=300,
                        required=True,
                        widget=forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Book Name'}))
    series_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )
    authors = forms.ModelMultipleChoiceField(label="Authors",
                                widget=forms.SelectMultiple(attrs={'multiple': True,
                                                                    'class': 'form-control'}),
                                queryset=Auther.objects.all())
    detail = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'placeholder': "Detail of the book"}))

    class Meta:
        model = Page
        fields = ('name', 'image', 'series_number')