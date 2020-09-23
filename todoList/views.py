from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import TodoItem
from django.utils import timezone


def todoView(request):
    all_todo = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items': all_todo})


def addTodo(request):
    c = request.POST['content']
    a = request.POST['author']
    new_item = TodoItem(content=c, date_created=timezone.now(), author=a)
    new_item.save()
    return HttpResponseRedirect(reverse('todoList:index'))


def deleteTodo(request, todo_id):
    c = get_object_or_404(TodoItem, pk=todo_id)
    c.delete()
    return HttpResponseRedirect(reverse('todoList:index'))
