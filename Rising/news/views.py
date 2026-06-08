from django.shortcuts import render
from .models import Articles

def news(request):
    news = Articles.objects.all()
    return render(request, 'news/news.html', {'news': news})
