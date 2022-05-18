from django import template

register = template.Library()


@register.filter()
def censor(value):
    text = str(value).replace('информация', ''.join(['*' for i in range(len('информация'))]))
    return text

