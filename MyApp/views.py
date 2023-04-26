from django.shortcuts import render, redirect

from MyApp.models import ToDoItem

def index(request):
    context = {
        'todo_list': ToDoItem.objects.all()
    }
    return render(request, 'MyApp/index.html', context)

def do(request, id):
    todo = ToDoItem.objects.get(id=id)
    todo.done = True
    todo.save()
    return redirect('/')

def undo(request, id):
    todo = ToDoItem.objects.get(id=id)
    todo.done = False 
    todo.save()
    return redirect('/')