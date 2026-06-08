from django.shortcuts import render
from .models import Articles

def news(request):
    news = Articles.objects.order_by('date') # Создали переменную с данными из таблицы Articles. all() означает все данные
    # Если поставить - перед title сортирует в обратном порядке
    # [:2] указывает количество блоков
    return render(request, 'news/news.html', {'news': news}) # Добавили ключ для работы с articles
