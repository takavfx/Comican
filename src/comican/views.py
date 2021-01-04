import os
import zipfile
import tempfile
import logging

from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import (
    ListView,
    CreateView
)
from django.views.generic.edit import FormView
from django.urls import reverse
from django.template import RequestContext
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)
from django.contrib import messages
from django.contrib.auth import (
    login,
    authenticate
)
from django.db.models import Q

from .forms import (
    AddBookForm,
    UserCreationForm
)
from .models import (
    Circle,
    Author,
    Book,
    Page,
    TagCategory,
    Tag,
    Copyright,
    Series,
    Character
)


logger = logging.getLogger(__name__)


class UploadView(FormView):
    form_class = AddBookForm
    # template_name = 'comican/uploader.html'  # Replace with your template.
    success_url = '#'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        logger.debug(form_class)
        logger.debug(form)
        logger.debug(files)
        if form.is_valid():
            for f in files:
                print(f)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def upload_pages(self, f):
        name, ext = os.path.splitext(os.path.basename(f))
        temp = tempfile.gettempdir() / 'comican'

        if ext in ['.zip']:
            with zipfile.ZipFile(f) as existing_zip:
                existing_zip.extractall('data/temp/ext')


class Create_account(CreateView):
    """
    docstring
    """
    def post(self, request, *args, **kwargs):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect('/')
        return render(request, 'create_account.html', {'from', form,})

    def get(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        return render(request, 'create_account.html', {'form': form,})



def unzip_upload(filename):
    pass


def index(request):

    add_book_form = AddBookForm(request.POST)

    if request.method == 'POST':
        print('Uploading')
        print(dir(request))
        print(request.POST.keys())
        print(request.FILES.getlist('image'))
        print(request.POST.get('authors'))

        images = request.FILES.getlist('image', False)

        book = Book(
            name=request.POST['name'],
            image=images,
            detail=request.POST['detail'],
            favorite=False,
        )

        if request.POST['series']:
            book.series = Series.objects.get(pk=request.POST['series'])

        if request.POST['series_number']:
            book.series_number = request.POST.get('series_number', 1)
        else:
            book.series_number = 1

        book.save()

    ## Get items and render
    latest_book_list = Book.objects.order_by('-created_at')
    query = request.GET.get('query')
    if query:
        latest_book_list = latest_book_list.filter(
            Q(name__icontains=query)
        )

    ## Pagination
    paginator = Paginator(latest_book_list, 27)
    p = request.GET.get('page', 1)
    try:
        books = paginator.page(p)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    context = {
        'books': books,
        'add_book_form': add_book_form,
    }

    return render(request, 'comican/index.html', context)


def book(request, book_id):
    ## Get items and render
    book = get_object_or_404(Book, pk=book_id)
    add_book_form = AddBookForm(request.POST)
    context = {
        'book': book,
        'add_book_form': add_book_form,
    }
    return render(request, 'comican/book.html', context)


def page(request, book_id, page_number):
    ## Get items and render
    book = get_object_or_404(Book, pk=book_id)
    book_page = Book.objects.get(pk=book_id).pages.order_by('page_number')[page_number-1]
    page = get_object_or_404(Page, pk=book_page.id)
    add_book_form = AddBookForm(request.POST)
    context = {
        'book': book,
        'page': page,
        'add_book_form': add_book_form,
    }
    return render(request, 'comican/page.html', context)


def add_book(request):
    if request.method == 'POST':
        print(request)
        image_form = AddBookForm(request)
        if image_form.is_valid():
            portfolio_images = request.FILES.getlist('image', False)
            for image in portfolio_images:
                image_instance = Page(
                    image=image,
                )
                image_instance.save()
                print("success save images.")


def circles(request):
    circles = Circle.objects.order_by('-created_at')
    context = {
        'circles': circles
    }
    return render(request, 'comican/circles.html', context)


def tags(request):
    tags = Tag.objects.order_by('-created_at')
    context = {
        'tags': tags
    }
    return render(request, 'comican/tags.html', context)

def authors(request):
    authors = Author.objects.order_by('-created_at')
    context = {
        'authors': authors
    }
    return render(request, 'comican/authors.html', context)