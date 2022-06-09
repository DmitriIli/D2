from django.urls import path
# Импортируем созданное нами представление
from .views import *

urlpatterns = [
    # path — означает путь.
    # В данном случае путь ко всем товарам у нас останется пустым,
    # чуть позже станет ясно почему.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('news/all/', NewsList.as_view(), name='news'),
    path('article/all/', ArticleList.as_view(), name='article'),
    path('<int:pk>', PostDetail.as_view(), name='postdetail'),
    path('search/', SearchList.as_view(), name='search'),
    path('news/create/', AddPost.as_view()),
    path('<int:pk>/edit', UpdatePost.as_view(), name='edit'),
    path('<int:pk>/delete', DeletePost.as_view(), name='delete'),
    path('article/create/', AddPost.as_view()),
    path('', MainView.as_view(), name='main'),

]
