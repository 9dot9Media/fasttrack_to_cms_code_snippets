# Contents of mycms/urls.py
from django.conf.urls import include, url

from django.contrib import admin

from cms import views
from mycms import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.home, name='home'),

    url(r'^articles/$', views.test_view, name='articles-list'),
    url(r'^articles/(?P<slug>[\w-]+)$', views.test_view, name='articles-detail'),

    url(r'^categories/$', views.test_view, name='categories-list'),
    url(r'^categories/(?P<slug>[\w-]+)$', views.test_view, name='categories-detail'),

    url(r'^tags/$', views.test_view, name='tags-list'),
    url(r'^tags/(?P<slug>[\w-]+)$', views.test_view, name='tags-detail'),

    url(r'^galleries/$', views.test_view, name='galleries-list'),
    url(r'^galleries/(?P<slug>[\w-]+)$', views.test_view, name='galleries-detail'),

    url(r'^authors/$', views.test_view, name='authors-list'),
    url(r'^authors/(?P<slug>[\w-]+)$', views.test_view, name='authors-detail'),

    url(r'^image/(?P<slug>[\w-]+)$', views.test_view, name='image-detail'),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

]
