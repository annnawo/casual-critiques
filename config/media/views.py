from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db.models import Count
from .models import *

# Create your views here.

def home(request):
    books = Book.objects.all().order_by('-date_finished').values()
    return render(request, 'media/media_list.html', {'books': books})

def all_media(request):
    books = Book.objects.all().order_by('-date_finished').values()
    return render(request, 'media/media_list.html', {'books': books})

def book_detail(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    highlights = book.highlights.all().order_by('page_number').values()
    return render(request, 'media/book_detail.html', {'book': book, 'highlights':highlights})

def all_highlights(request):
    books = Book.objects.annotate(num_highlights=Count('highlights')).order_by('num_highlights')
    return render(request, 'media/all_highlights.html', {'books': books})