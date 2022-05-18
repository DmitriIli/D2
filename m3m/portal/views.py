from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-datetime_of_topic'
    # queryset = Post.objects.order_by('-datetime_of_topic')
    template_name = 'news.html'
    context_object_name = 'news_list'


class NewsDetail(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'
