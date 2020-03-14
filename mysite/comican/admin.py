from django.contrib import admin

from .models import Circle, Author, Book, Page, TagCategory, Tag, Copyright, Series, Character, Publisher



class BookAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'series_number', 'favorite')
    list_filter = ['favorite']


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['book', 'page_number', 'image']}),
        ('Meta Data', {'fields': ['copyrights', 'tags', 'bookmark']})
    ]

    # list_display = ('name', 'bookmark')



def register_models():
    
    reg_model_sets = [
        [Circle],
        [Author],
        [Book, BookAdmin],
        [Page, PageAdmin],
        [TagCategory],
        [Tag],
        [Copyright],
        [Series],
        [Character],
        [Publisher]
    ]

    for reg_model_set in reg_model_sets:
        if not len(reg_model_set) == 2:
            admin.site.register(reg_model_set[0])
        else:
            admin.site.register(reg_model_set[0], reg_model_set[1])


def main():
    register_models()

main()