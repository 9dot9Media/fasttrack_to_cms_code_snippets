# Contents of cms/admin.py
from django.contrib import admin

from cms.models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category',
                    'creation_date', 'edit_date',
                    'publish_status',)
    list_editable = ('publish_status',)
    list_filter = ('category',
                   'creation_date',
                   'publish_status',)
    search_fields = ['author__first_name',
                     'author__last_name',
                     'author__email',
                     'author__username',
                     'title', 'content', ]


admin.site.register(Article, ArticleAdmin)
