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
    # Rlation
    circles = models.ManyToManyField(Circle, blank=True)

    # Unique
    name = models.CharField(max_length=300)
    detail = models.TextField(blank=True)
    web = models.URLField(blank=True)
    activity_started = models.DateField('Activity Started')
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
    # Rlation
    category = models.ForeignKey(TagCategory, on_delete=models.CASCADE)

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
    # Rlation
    copyright = models.ForeignKey(Copyright, on_delete=models.CASCADE, blank=True, null=True)

    # Unique
    name = models.CharField(max_length=300)
    detail = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/uploads/%Y/%m/%d/thm/', blank=True)
    created_at = models.DateTimeField('Date Created', auto_now_add=True)
    updated_at = models.DateTimeField('Date Updated', auto_now=True)

    def __str__(self):
        return


class Series(models.Model):
    # Rlation
    # Unique
    name = models.CharField(max_length=300)
    detail = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    # Rlation
    authors = models.ManyToManyField(Auther, blank=True, null=True)
    series = models.ForeignKey(Series, blank=True, null=True, on_delete=models.CASCADE)

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
    # Rlation
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    copyrights = models.ManyToManyField(Copyright, blank=True, null=True)

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





