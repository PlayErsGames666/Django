from django.shortcuts import render
from .models import Articles

def news(request):
    news = Articles.objects.all() # Создали переменную с данными из таблицы Articles. all() означает все данные
    return render(request, 'news/news.html', {'news': news}) # Добавили ключ для работы с articles
