from django.contrib import admin
from .models import Author, Book, Highlight

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title")}

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Highlight)