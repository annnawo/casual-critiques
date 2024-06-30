from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('all_media/', views.all_media, name='all_media'),
]