from django.views.generic import ListView, DetailView
from .models import Post
from .filters import NewsFilter
from datetime import datetime
from pprint import pprint


class NewsList(ListView):
    model = Post
    ordering = '-datetime_of_topic'
    # queryset = Post.objects.order_by('-datetime_of_topic')
    template_name = 'news.html'
    context_object_name = 'news_list'
    paginate_by = 1



class NewsDetail(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'

class SearchList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'query_set'

    # Переопределяем функцию получения списка новостей
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список новостей
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset