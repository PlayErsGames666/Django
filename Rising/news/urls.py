from django.urls import path
from . import views

urlpatter = [
    path('', views.news, name = 'news')
]