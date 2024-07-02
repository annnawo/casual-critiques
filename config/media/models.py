from django.db import models

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
    
    def __str__(self):
        return self.title

    