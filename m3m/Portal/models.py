from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


# Create your models here.

class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)

    def update_rating(self):
        rating_post = self.post_set.aggregate(post_rating=Sum('rating'))
        r_post = 0
        r_post += rating_post.get('post_rating')

        rating_comment = self.author.comment_set.aggregate(comment_rating=Sum('rating'))
        r_comment = 0
        r_comment += rating_comment.get('comment_rating')

        self.rating = r_post * 3 + r_comment
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    news = 'NW'
    article = 'AT'

    TYPES = [
        (news, 'новости'),
        (article, 'статья'),
    ]

    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    types_of_topic = models.CharField(max_length=2, default=news, choices=TYPES)
    datetime_of_topic = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=256, default='title')
    text = models.TextField(default='text')
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[:123]}...'


class PostCategory(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default='comment text')
    datetime_comment = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
