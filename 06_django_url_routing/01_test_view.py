# Contents of mycms/urls.py
from django.conf.urls import include, url

from django.contrib import admin

from cms import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^test/', views.test_view),

]
