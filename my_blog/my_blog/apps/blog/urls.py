from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('add_article', views.add_article, name='add_article'),
    path('<int:article_id>/', views.article, name='article'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment')
]
