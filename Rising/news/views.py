from django.shortcuts import render
from .models import Articles

def news(request):
    news_list = Articles.objects.order_by('date') # Создали переменную с данными из таблицы Articles. all() означает все данные
    # Если поставить - перед title сортирует в обратном порядке
    # [:2] указывает количество блоков
    data = {
        'news': 'News' ,
        'news': news_list
    }
    return render(request, 'news/news.html', data) # Добавили ключ для работы с articles

def create(request):
    data = {
        'title_name': 'Create Posts'
    }
    return render(request, 'news/create.html', data)