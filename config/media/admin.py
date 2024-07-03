from django.contrib import admin
from .models import Author, Book


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title")}

admin.site.register(Book)
admin.site.register(Author)