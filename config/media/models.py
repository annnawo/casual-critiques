from django.db import models
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, null=False)
    authors = models.ManyToManyField(Author, related_name='books')
    kindle = models.BooleanField(null=True)
    physical = models.BooleanField(null=True)
    date_finished = models.DateField()
    times_read = models.IntegerField()
    year_published = models.PositiveIntegerField(null=True)
    svg_path = models.CharField(max_length=200, null=False)
    jpg_path = models.CharField(max_length=200, null=False)
    contains_spoilers = models.BooleanField(null=True)
    highlights_uploaded = models.BooleanField(null=True)
    notes_uploaded = models.BooleanField(null=True)
    slug = models.SlugField(default="", null=False)
    
    def __str__(self):
        return self.title
    
class Highlight(models.Model):
    book = models.ForeignKey(Book, related_name='highlights', on_delete=models.CASCADE)
    content = models.TextField()
    page_number = models.PositiveIntegerField(null=True, blank=True)
    location = models.PositiveIntegerField(null=True, blank=True)
    