# The following lines of code are intended to be run in the Django shell: `python3 manage.py shell`
# Before running them it would be best to have some data in the database that you can play with.
# Here is how you can import some test data into your database:
# 1. Download the test_data_1.json file from this folder in the repository
# 2. Run `python3 manage.py loaddata test_data_1.json` to load the data.
# You should have already run the `makemigrations` and `migrate` commands before this.

from django.contrib.auth.models import User

from cms.models import Article

Article.objects.all()

User.objects.all()

Article.objects.filter(publish_status=True)

Article.objects.exclude(publish_status=False)

Article.objects.filter(title__startswith='The')

Article.objects.filter(author__first_name__startswith='V')

Article.objects.filter(title__startswith='A', publish_status=False)
Article.objects.filter(title__startswith='A').filter(publish_status=False)

Article.objects.order_by('title')
