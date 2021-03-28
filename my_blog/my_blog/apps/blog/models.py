from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length=200)
    article = models.TextField('Статья')
    publication_date = models.DateTimeField('Дата публикации')
    article_author = models.CharField('Автор статьи', max_length=50, default='')

    def __str__(self):
        return self.article_title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField('Комментарий к статье', default='')
    comment_author = models.CharField('Автор комментария', max_length=50, default='')
    publication_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f'Автор комментария: {self.comment_author}'

