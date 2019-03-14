from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import TodoItem
from datetime import datetime


def todoView(request):
    todos = TodoItem.objects.all().order_by('-todo_time', 'todo_completed')
    return render(request, 'todo.html', {'todos': todos})

def addTodo(request):
    format = '%b %d, %Y %I:%M %p'
    date = datetime.strptime((request.POST['date'] + ' ' + request.POST['time']), format)
    todo = TodoItem(
        todo_content=request.POST['content'],
        todo_time=date
    )
    todo.save()
    return HttpResponseRedirect('/todo/')

def delTodo(request):
    todo = TodoItem.objects.get(todo_id = request.POST['id'])
    todo.delete()
    return HttpResponseRedirect('/todo/')


def editTodo(request):
    todo = TodoItem.objects.get(todo_id = request.POST['id'])
    todo.todo_content = request.POST['content']
    todo.save()
    return HttpResponseRedirect('/todo/')

def viewTodo(request):
    data = list(TodoItem.objects.values())
    return JsonResponse({'data': data})

def toggleTodo(request):
    todo = TodoItem.objects.get(todo_id = request.POST['id'])
    todo.todo_completed = not todo.todo_completed
    todo.save()
    return HttpResponseRedirect('/todo/')