from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from .models import Article
from django.utils import timezone


class ArticleFrom(ModelForm):
    class Meta:
        model = Article
        fields = ['article_title', 'article']
        widgets = {'article_title': TextInput(attrs={
            'placeholder': 'Название статьи',
            'class': 'from-control'
        }),
            'article': Textarea(attrs={
                'placeholder': 'Статья',
                'class': 'from-control'
            }),
            'publication_date': DateTimeInput(attrs={
                'class': 'from-control',
                'value': timezone.now().date()
            })
        }
