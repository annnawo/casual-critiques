from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('all_media/', views.all_media, name='all_media'),
    path('book/<slug:book_slug>/', views.book_detail, name='book_detail'),
    path('all_highlights/', views.all_highlights, name='all_highlights'),
]