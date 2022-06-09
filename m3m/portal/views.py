from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView
from .forms import PostForm
from .models import Post
from .filters import NewsFilter
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class NewsList(ListView):
    # model = Post
    # ordering = '-datetime_of_topic'
    queryset = Post.objects.filter(
        types_of_topic__iexact='NW'
    ).order_by('-datetime_of_topic')
    template_name = 'news.html'
    context_object_name = 'news_list'
    paginate_by = 10


class ArticleList(ListView):
    # model = Post
    # ordering = '-datetime_of_topic'
    queryset = Post.objects.filter(
        types_of_topic__iexact='AT'
    ).order_by('-datetime_of_topic')
    template_name = 'article.html'
    context_object_name = 'article_list'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            return redirect('search')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class SearchList(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search_set'
    paginate_by = 1

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
        return context


# def add_news(request):
#     form = PostForm()
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/news')
#
#     return render(request, 'edit_post.html', {'form': form})

class AddPost(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'edit_post.html'

    permission_required = ('portal.add_post')

    def form_valid(self, form):
        post = form.save(commit=False)
        current_url = self.request.path
        if current_url.find('/news/'):
            post.types_of_topic = 'NW'
        elif current_url.find('/article/'):
            post.types_of_topic = 'AT'
        return super().form_valid(form)


class UpdatePost(PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'edit_post.html'
    permission_required = ('portal.change_post')

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            return redirect('search')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class DeletePost(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    permission_required = ('portal.delete_post')
    success_url = reverse_lazy('search')


    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            return redirect('search')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class MainView(TemplateView):
    template_name = 'main.html'
