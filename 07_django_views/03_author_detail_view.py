# Contents of cms/views.py
from django.contrib.auth.models import User
from django.views.generic import DetailView


class AuthorDetail(DetailView):
    model = User

    def get_slug_field(self):
        return 'username'
