from django.db.models import Count
from cms.models import Tag

Tag.objects.annotate(num_articles=Count('article'))
