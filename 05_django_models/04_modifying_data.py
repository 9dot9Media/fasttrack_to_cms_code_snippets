from cms.models import Article

article2 = Article.objects.get(pk=11)

Article.objects.filter(author__first_name__startswith='K')

Article.objects.filter(author__first_name__startswith='K').update(publish_status=True)
