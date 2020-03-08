from django import forms

from .models import Page, Book, Auther, Series

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class AddBookForm(forms.ModelForm):
    name = forms.CharField(label='Name',
                        max_length=300,
                        required=True,
                        widget=forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Book Name'}))
    series = forms.ModelChoiceField(
            queryset=Series.objects.all(),
            label="Series",
            widget=forms.Select(
                attrs={'class': 'form-control'}
            )
        )
    series_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )
    authors = forms.ModelMultipleChoiceField(
            queryset=Auther.objects.all(),
            label="Authors",
            widget=forms.SelectMultiple(
                attrs={
                    'multiple': True,
                    'class': 'form-control'}
                    )
        )
    detail = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'placeholder': "Detail of the book"}))

    class Meta:
        model = Page
        fields = ('name', 'image', 'series_number')