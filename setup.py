import json
from django.contrib.auth.models import User
from MyApp.models import ToDoItem

if User.objects.count() == 0:
    username = 'admin'
    password = '1234'
    email = 'admin@example.com'

    user = User(
        username=username,
        email=email
    )

    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True

    user.save()

ToDoItem.objects.create(text="Lorem ipsum dolor sit")
ToDoItem.objects.create(text="Curabitur non nunc et")
ToDoItem.objects.create(text="Maecenas condimentum")