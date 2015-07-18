####################################################################################################
# Contents for mycms/urls.py
url(r'^articles/([\w-]+)$', views.article_detail, name='articles-details')
####################################################################################################

####################################################################################################
# Function-based article detail view
# Contents of cms/views.py
from cms.models import Article


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    html = """
    <html>
    <head><title>{title}</title></head>
    <body>
    <h1>{title}</h1>
    <p>Author: {author}</p>
    {content}
    </body>
    </html>
    """
    response = html.format(
        title=article.title,
        author=article.author.username,
        category=article.category.name,
        content=article.content)
    return HttpResponse(response)
####################################################################################################

####################################################################################################
# Function-based article detail view using templates
# Contents of cms/views.py
from django.shortcuts import render


def article_detail(request, article_slug):
    article = Article.objects.get(slug=article_slug)
    context = {'article': article}
    return render(request, 'article_detail.html', context)
####################################################################################################


####################################################################################################
# Class-based article detail view
# Contents of cms/views.py
from django.views.generic import View
from django.http import HttpResponse


class ArticleDetail(View):
    html = """
           <html>
           <head><title>{title}</title></head>
           <body>
           <h1>{title}</h1>
           <p>Author: {author}</p>
           <p>Category: {category}</p>
           {content}
           </body>
           </html>
           """

    def get(self, request, article_slug):
        article = Article.objects.get(slug=article_slug)
        response = self.html.format(
            title=article.title,
            author=article.author.username,
            category=article.category.name,
            content=article.content)
        return HttpResponse(response)
####################################################################################################


####################################################################################################
# Class-based generic article detail view
# Contents of cms/views.py
from django.views.generic import DetailView


class ArticleDetail(DetailView):
    model = Article
####################################################################################################
