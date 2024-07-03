from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *

# Create your views here.

def home(request):
    books = Book.objects.all()
    print(books)
    return render(request, 'media/media_list.html', {'books': books})

def all_media(request):
    books = Book.objects.all()
    print(books)
    return render(request, 'media/media_list.html', {'books': books})

def book_detail(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    return render(request, 'media/book_detail.html', {'book': book})