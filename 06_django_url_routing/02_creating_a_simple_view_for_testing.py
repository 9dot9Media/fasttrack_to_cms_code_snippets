# Contents of cms/views.py
from django.http import HttpResponse


def test_view(request):
    return HttpResponse(
        'This URL is properly mapped.'
    )
