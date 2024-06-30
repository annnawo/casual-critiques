from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *

# Create your views here.

def home(request):
    return render(request, 'media/media_list.html')

def all_media(request):
    return render(request, 'media/media_list.html', {})
