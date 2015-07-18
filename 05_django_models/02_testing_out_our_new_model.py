# Run the following commands in the Django shell `python3 manage.py shell`

# Trying to create a new article. This will result in an error.
from cms.models import Article

article1 = Article()
article1.title = "New Article"
article1.content = "Test content"
article1.slug = "new-article"
article1.save()

# Creating a new user.
from django.contrib.auth.models import User

author1 = User()
author1.first_name = 'Aruna'
author1.last_name = 'Tank'
author1.email = 'aruna.tank@mailprovider.com'
author1.set_password('apassword')
author1.save()


# The above article can be saved now tha tis has an author attached.
article1.author = author1
article1.save()