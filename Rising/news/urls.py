from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name = 'news'),
    path('create/', views.create, name = 'create'),
    path('<int:pk>', views.NewDetailView.as_view(), name = 'news-detail'), # Создали динамическую ссылку, чтобы каждый id поста можно было просмотреть по отдельности
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name = 'news-update'), # Создали ссылку для обновление страницы
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name = 'news-delete')
]