import os
import zipfile
import tempfile
import logging

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from django.views.generic.edit import FormView
from django.urls import reverse
from django.template import RequestContext

from .forms import FileFieldForm, AddBookForm
from .models import Circle, Auther, Book, Page, TagCategory, Tag, Copyright, Series, Character


logger = logging.getLogger(__name__)


class Upload(FormView):
    form_class = AddBookForm
    template_name = 'comican/uploader.html'  # Replace with your template.
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


def index(request):
    latest_book_list = Book.objects.order_by('-created_at')[:20]
    upload_form = AddBookForm(request.POST)
    context = {
        'latest_book_list': latest_book_list,
        'upload_form': upload_form
    }
    return render(request, 'comican/index.html', context)


def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    upload_form = AddBookForm(request.POST)
    context = {
        'book': book,
        'upload_form': upload_form
    }
    return render(request, 'comican/book.html', context)


def page(request, book_id, page_number):
    book = get_object_or_404(Book, pk=book_id)
    book_page = Book.objects.get(pk=book_id).pages.all()[page_number-1]
    print(book_page)
    page = get_object_or_404(Page, pk=book_page.id)
    upload_form = AddBookForm(request.POST)
    context = {
        'book': book,
        'page': page,
        'upload_form': upload_form,
    }
    return render(request, 'comican/page.html', context)


def upload_sample(request):
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

