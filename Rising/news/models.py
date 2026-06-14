from django.db import models

class Articles(models.Model): # Создаём класс как таблицу в бд
    title = models.CharField('Title', max_length=50) # Добавляем название и максимальную длинну 50 символов
    announs = models.CharField('The Announcement', max_length=250) # Добавляем название и максимальную длинну 250 символов
    text = models.TextField() # Здесь уже используется метод textfield, в нём может быть от 1 000 символов и больше
    date = models.DateTimeField() # Добавляем дату и время

    def __str__(self): # Крч, выводит и название статьи, если его не будет то просто будет выводить id статью
        return f'News: {self.title}' # Добавляет к началу строки слово News

    def get_absolute_url(self): # абсолют url работает как переодресация, на какую страницу пойдёт сайт после обновлния
        return f'/news/{self.id}'

    class Meta: # Создали класс для смены названия в админ панели
        verbose_name = "New" # Назваение таблицы в ед числе
        verbose_name_plural = "News" # Назваение таблицы в мнж числе