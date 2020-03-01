from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf import settings

from .models import Circle, Auther, Book, Page, TagCategory, Tag, Copyright, Series, Character

# Create your views here.
def index(request):
    latest_book_list = Book.objects.order_by('-created_at')[:20]
    context = {'latest_book_list': latest_book_list}
    return render(request, 'comican/index.html', context)

def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'comican/book.html', {'book': book})