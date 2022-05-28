from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author_id',
            'post_category',
            'title',
            'text',
            'rating',
        ]

    def clean(self):
        cleaned_date = super().clean()
        title = cleaned_date.get('title')
        if title is not None and len(title) < 10:
            raise ValidationError({
                'title': 'описание меньше 10 символов'
            })

        text = cleaned_date.get('text')
        if text == title:
            raise ValidationError({
                'text': 'текст не должен быть равен заголовку'
            })
        elif text is not None and len(text) < 20:
            raise ValidationError({
                'text': 'статья слишком короткая'
            })

        return cleaned_date
