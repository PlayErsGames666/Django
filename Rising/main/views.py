from django.shortcuts import render
# from django.http import HttpResponse # Конвертрует html code для браузера

def index(request):
    data = { # переменная с данными которые передаються в шаблон(как в JSON)
        'title': 'Main Page',
        'values': ['Data', '10', 'Massive'],
        'obj': {
            'sex': 'male',
            'age': "22",
            'hobby': 'horsing'
        }
    }
    return render(request, 'main/index.html', data)

# Старый способ вызозова HTML
# def main(request): # Обязательно нужно получать хотя бы один параметр, иначе не будет работать
#     return HttpResponse("<h4>Дорога работает</h4>" \
#     "<a href=/index>Index</a>") # Конвертрует html code для браузера

def about(request):
    data = { # переменная с данными которые передаються в шаблон(как в JSON)
        'about': 'About Us'
    }
    return render(request, 'main/about.html', data)
