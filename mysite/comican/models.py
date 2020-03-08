from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill



class Circle(models.Model):
    # Unique
    name = models.CharField(max_length=300)
    activity_started = models.DateField('Activity Started', auto_now_add=True)
    on_active = models.BooleanField()
    created_at = models.DateTimeField('Date Created', auto_now_add=True)
    updated_at = models.DateTimeField('Date Updated', auto_now=True)

    def __str__(self):
        return self.name


class Auther(models.Model):
    # Relation
    circles = models.ManyToManyField(Circle, blank=True, related_name='authors')

    # Unique
    name = models.CharField(max_length=300)
    detail = models.TextField(blank=True)
    web = models.URLField(blank=True)
    activity_started = models.DateField('Activity Started', blank=True)
    on_active = models.BooleanField()
    created_at = models.DateTimeField('Date Created', auto_now_add=True)
    updated_at = models.DateTimeField('Date Updated', auto_now=True)

    def __str__(self):
        return self.name



class Publisher(models.Model):
    # Unique
    name = models.CharField(max_length=300)
    detail = models.TextField(blank=True)
    web = models.URLField(blank=True)
    activity_started = models.DateField('Activity Started', blank=True)
    on_active = models.BooleanField()
    created_at = models.DateTimeField('Date Created', auto_now_add=True)
    updated_at = models.DateTimeField('Date Updated', auto_now=True)

    def __str__(self):
        return self.name



class TagCategory(models.Model):
    # Unique
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField('Date Created', auto_now_add=True)
    updated_at = models.DateTimeField('Date Updated', auto_now=True)

    def __str__(self):
        return self.name



class Tag(models.Model):
    # Relation
    category = models.ForeignKey(TagCategory, on_delete=models.CASCADE, related_name='tags')

    # Unique
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField('Date Created', auto_now_add=True)
    updated_at = models.DateTimeField('Date Updated', auto_now=True)

    def __str__(self):
        return self.name



class Copyright(models.Model):
    # Unique
    name = models.CharField(max_length=200)
    detail = models.TextField(blank=True)
    web = models.URLField(blank=True)
    created_at = models.DateTimeField('Date Created', auto_now_add=True)
    updated_at = models.DateTimeField('Date Updated', auto_now=True)
    
    def __str__(self):
        return self.name


class Character(models.Model):
    # Relation
    copyright = models.ForeignKey(Copyright,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
                                related_name='characters')

    # Unique
    name = models.CharField(max_length=300)
    detail = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/uploads/%Y/%m/%d/thm/', blank=True)
    created_at = models.DateTimeField('Date Created', auto_now_add=True)
    updated_at = models.DateTimeField('Date Updated', auto_now=True)

    def __str__(self):
        return


class Series(models.Model):
    # Relation
    # Unique
    name = models.CharField(max_length=300)
    detail = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    # Relation
    authors = models.ManyToManyField(Auther, blank=True, related_name='books')
    series = models.ForeignKey(Series,
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE,
                                related_name='book')

    # Unique
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/uploads/%Y/%m/%d/thm/')
    thumbnail = ImageSpecField(source='image',
                                processors=[ResizeToFill(336, 522)],
                                format='JPEG',
                                options={'quality': 90})
    detail = models.TextField(blank=True)
    favorite = models.BooleanField()
    series_number = models.IntegerField(blank=True)
    pub_date = models.DateField('Date Book Published', blank=True, null=True)
    created_at = models.DateTimeField('Date Created', auto_now_add=True)
    updated_at = models.DateTimeField('Date Updated', auto_now=True)


    def __str__(self):
        return self.name



class Page(models.Model):
    # Relation
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='pages')
    tags = models.ManyToManyField(Tag, blank=True, related_name='pages')
    copyrights = models.ManyToManyField(Copyright, blank=True, related_name='pages')

    #Unique
    page_number = models.IntegerField()
    image = models.ImageField(upload_to='media/uploads/%Y/%m/%d/thm/')
    thumbnail = ImageSpecField(source='image',
                                processors=[ResizeToFill(336, 522)],
                                format='JPEG',
                                options={'quality': 90})
    bookmark = models.BooleanField()
    last_view = models.DateTimeField('Date Book Published', auto_now_add=True)
    created_at = models.DateTimeField('Date Created', auto_now_add=True)
    updated_at = models.DateTimeField('Date Updated', auto_now=True)

    def __str__(self):
        return self.book.name + '_P' + str(self.page_number)




