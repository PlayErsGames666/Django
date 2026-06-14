from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news(request):
    news_list = Articles.objects.all() # Создали переменную с данными из таблицы Articles. all() означает все данные
    # Если поставить - перед title сортирует в обратном порядке
    # [:2] указывает количество блоков
    data = {
        'news': 'News' ,
        'news': news_list
    }
    return render(request, 'news/news.html', data) # Добавили ключ для работы с articles

class NewDetailView(DetailView): # класс в котором можно будет просмотреть пост детально
    model = Articles # Модель к которой обращается 
    template_name = 'news/details_view.html' # имя шаблона на который надо перейти
    context_object_name = 'article' # ключ который можно использовать для обращения к данным из DB


class NewsUpdateView(UpdateView): # класс в котором можно обновить данные поста
    model = Articles # Модель к которой обращается 
    template_name = 'news/create.html' # имя шаблона на который надо перейти

    form_class = ArticlesForm # Класс формы которую сделали в forms.py 

class NewsDeleteView(DeleteView): # класс в котором можно удалить данные поста
    model = Articles # Модель к которой обращается 
    success_url = '/news/' # переход на страницу после удаления
    template_name = 'news/news-delete.html' # имя шаблона на который надо перейти

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