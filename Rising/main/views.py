from django.shortcuts import render
from django.http import HttpResponse # Конвертрует html code для браузера

def index(request): # Обязательно нужно получать хотя бы один параметр, иначе не будет работать
    return HttpResponse("<h4>Дорога работает</h4>" \
    "<a href=/about>About U</a>") # Конвертрует html code для браузера

def about(request):
    return HttpResponse("<h4>About your mother LS</h4>")
