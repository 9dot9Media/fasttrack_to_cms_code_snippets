# Contents of cms/admin.py
from django.contrib import admin

from cms.models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category',
                    'creation_date', 'edit_date',
                    'publish_status',)


admin.site.register(Article, ArticleAdmin)
