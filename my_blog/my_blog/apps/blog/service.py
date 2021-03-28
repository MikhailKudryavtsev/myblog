from .models import Article, User
from django.utils import timezone


def add_user_to_db(request):
    user = User(user_name=request.POST['username'], user_password=request.POST['password'], date_registration=timezone.now())
    user.save()


def add_article_to_db(request):
    article = Article(article_title=request.POST['name'],
                      article=request.POST['article'],
                      publication_date=timezone.now())
    article.save()
