from django import forms

from .models import Page, Book, Author, Series

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class AddBookForm(forms.ModelForm):
    template_name = 'comican/uploader.html'
    # name = forms.CharField(label='Name',
    #                     max_length=300,
    #                     required=True,
    #                     widget=forms.TextInput(attrs={'class': 'form-control',
    #                                                 'placeholder': 'Book Name'}))
    # series = forms.ModelChoiceField(
    #         queryset=Series.objects.all(),
    #         label="Series",
    #         widget=forms.Select(
    #             attrs={'class': 'form-control'}
    #         ),
    #         required=False
    #     )
    # series_number = forms.IntegerField(
    #         widget=forms.NumberInput(attrs={'class': 'form-control'}),
    #     )
    # image = forms.ImageField(
    #     widget=forms.ClearableFileInput(attrs={'multiple': True}),
    # )
    # authors = forms.ModelMultipleChoiceField(
    #         queryset=Author.objects.all(),
    #         label="Authors",
    #         widget=forms.SelectMultiple(
    #             attrs={
    #                 'multiple': True,
    #                 'class': 'form-control'}
    #                 ),
    #         required=False
    #     )
    # detail = forms.CharField(
    #     required=False,
    #     widget=forms.Textarea(
    #         attrs={'class': 'form-control',
    #             'placeholder': "Detail of the book"}))


    class Meta:
        model = Book
        fields = '__all__' 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"



class AddPageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"