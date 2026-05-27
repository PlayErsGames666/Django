from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main),
    path('index', views.index),
    path('about', views.about)
]