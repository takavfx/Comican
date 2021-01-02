import os
import logging

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

logger = logging.getLogger(__name__)
logger.info('TEST')

urlpatterns = [
    path('', views.index, name='index'),
    path('books/<int:book_id>', views.book, name='book'),
    path('books/<int:book_id>/<int:page_number>', views.page, name='page'),
    path('circles/', views.circles, name='circles'),
    path('tags/', views.tags, name='tags'),
    path('authors/', views.authors, name='authors'),
]