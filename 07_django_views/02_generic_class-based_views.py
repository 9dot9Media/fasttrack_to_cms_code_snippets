# Contents of cms/views.py
from django.views.generic import ListView

from cms.models import Article


class ArticleList(ListView):
    model = Article


class ArticleList(ListView):
    queryset = Article.objects.filter(publish_status=True)
