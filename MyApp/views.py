from django.shortcuts import render 

from MyApp.models import ToDoItem

def index(request):
    context = {
        'todo_list': ToDoItem.objects.all()
    }

    return render(request, 'MyApp/index.html', context)