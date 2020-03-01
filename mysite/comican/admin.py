from django.contrib import admin

from .models import Circle, Auther, Book, Page, TagCategory, Tag, Copyright, Series, Character
reg_models = [
    Circle,
    Auther,
    Book,
    Page,
    TagCategory,
    Tag,
    Copyright,
    Series,
    Character
]

def register_models(reg_models):
    for reg_model in reg_models:
        admin.site.register(reg_model)

register_models(reg_models)