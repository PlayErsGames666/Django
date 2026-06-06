from django.db import models

class Articles(models.Model): # Создаём класс как таблицу в бд
    title = models.CharField('Title', max_length=50) # Добавляем название и максимальную длинну 50 символов
    announs = models.CharField('The Announcement', max_length=250) # Добавляем название и максимальную длинну 250 символов
    text = models.TextField() # Здесь уже используется метод textfield, в нём может быть от 1 000 символов и больше
    date = models.DateTimeField() # Добавляем дату и время

    def __str__(self): # На след уроке объяснит
        return self.title
