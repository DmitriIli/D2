from django import template

register = template.Library()


@register.filter()
def censor(value):
    text = str(value).replace('информация', ''.join(['*' for i in range(len('информация'))]))
    return text

#
# @register.filter()
# def add_end(value, inp='1'):
#     return f'{value}  {inp}'
