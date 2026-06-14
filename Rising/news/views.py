from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView

def news(request):
    news_list = Articles.objects.all() # Создали переменную с данными из таблицы Articles. all() означает все данные
    # Если поставить - перед title сортирует в обратном порядке
    # [:2] указывает количество блоков
    data = {
        'news': 'News' ,
        'news': news_list
    }
    return render(request, 'news/news.html', data) # Добавили ключ для работы с articles

class NewDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


def create(request):
    error = ""
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = '4xx error'

    form = ArticlesForm()
    data = {
        'title_name': 'Create Posts',
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)