from django.db.models import Count

from cms.models import Category

Category.objects.annotate(num_articles=Count('article'))

categories = Category.objects.annotate(
    num_articles=Count('article')
).order_by('-num_articles')[:2]

####################################################################################################
# Contents of cms/views.py
from django.shortcuts import render

from cms.models import Article
from cms.models import Category


def home(request):
    articles = Article.objects.filter(publish_status=True)[:10]
    categories = Category.objects.annotate(
        num_articles=Count('article')
    ).order_by('-num_articles')[:2]
    context = {
        'articles': articles,
        'categories': categories
    }
    return render(request, 'cms/home.html', context)

####################################################################################################
