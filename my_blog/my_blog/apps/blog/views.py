from django.contrib import auth
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from .models import Article, User
from .service import add_user_to_db, add_article_to_db


def home(request):
    """Выводит домашнюю страницу"""
    return render(request, 'index.html', {'article_list': Article.objects.all(),
                                          'username': auth.get_user(request).username})


def add_article(request):
    """Добавляет статью"""
    if request.method == 'POST':
        add_article_to_db(request)
        return redirect('/')
    context = {
        'article': Article.objects.all()
    }
    return render(request, 'add_article.html', context)


def article(request, article_id):
    """Выводит статью с id равной article_id"""
    a = check_article(article_id)
    return render(request, 'article.html', {'article': a,
                                            'comment_list': a.comment_set.order_by('-id')[:10]})


def leave_comment(request, article_id):
    """Добавляет комментарий к статье с id равной article_id"""
    a = check_article(article_id)
    a.comment_set.create(comment_author=request.POST.get('author'),
                         comment=request.POST.get('comment'),
                         article_id=article_id,
                         publication_date=timezone.now())
    return HttpResponseRedirect(reverse('blog:article', args=(a.id, )))


def check_article(article_id):
    """Проеряет существует ли статья с id равной article_id"""
    try:
        a = Article.objects.get(id=article_id)
    except Exception as e:
        raise Http404('Статья не найдена!')
    return a



