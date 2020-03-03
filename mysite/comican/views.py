import os
import zipfile
import tempfile
import logging

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from django.views.generic.edit import FormView
from django.urls import reverse

from .forms import FileFieldForm
from .models import Circle, Auther, Book, Page, TagCategory, Tag, Copyright, Series, Character


logger = logging.getLogger(__name__)

# class FileFieldView(FormView):
#     form_class = FileFieldForm
#     template_name = 'comican/upload.html'

#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')

#         if form.is_valid():
#             for f in files:
#                 self.upload_pages(f, files)
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)


#     def upload_pages(self, f):
#         name, ext = os.path.splitext(os.path.basename(f))
#         temp = tempfile.gettempdir() / 'comican'

#         if ext in ['.zip']:
#             with zipfile.ZipFile(f) as existing_zip:
#                 existing_zip.extractall('data/temp/ext')


def index(request):
    latest_book_list = Book.objects.order_by('-created_at')[:20]
    context = {'latest_book_list': latest_book_list}
    return render(request, 'comican/index.html', context)

def book(request, book_id):
    return HttpResponse("You're looking at book %s." % book_id)
    # book = get_object_or_404(Book, pk=book_id)
    # return render(request, 'comican/book.html', {'book': book})

def page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, 'comican/page.html', {'page': page})