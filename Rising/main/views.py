from django.shortcuts import render
from django.http import HttpResponse # Конвертрует html code для браузера

def index(request): # Обязательно нужно получать хотя бы один параметр, иначе не будет работать
    return HttpResponse("<h4>Дорога работает</h4>") # Конвертрует html code для браузера


