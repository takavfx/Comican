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
    path('<int:book_id>/', views.book, name='book'),
    path('<int:page_id>/', views.page, name='page'),
    path('upload/', views.Upload, name='upload'),
]#  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)