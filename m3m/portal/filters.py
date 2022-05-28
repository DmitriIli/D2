import django_filters
from django_filters import FilterSet
from .models import Post


class NewsFilter(FilterSet):
    date = django_filters.DateTimeFilter(field_name='datetime_of_topic', lookup_expr='gt')
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    author = django_filters.NumberFilter(field_name='author_id', lookup_expr='exact')

    class Meta:
        model = Post
        fields = ['date', 'title', 'author']
