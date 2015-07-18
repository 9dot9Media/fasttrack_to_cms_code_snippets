# Contents of cms/admin.py
from django.contrib import admin
from cms.models import *

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Gallery)
admin.site.register(Image)