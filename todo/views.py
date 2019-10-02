from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

# Create your views here.
def todoView(request):

    all_todo_items = TodoItem.objects.all()
    return render(request,'todo.html',
    {'all_items':all_todo_items})

def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')
    # create new todo item object
    # Save
    # redirect the browser to "/todo/"

def deleteTodo(request, todo_id):
    item_del = TodoItem.objects.get(id=todo_id)
    item_del.delete()
    return HttpResponseRedirect('/todo/')