from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from datetime import datetime
from .models import TodoItem


def todoView(request):
    todos = TodoItem.objects.all().order_by('todo_completed', '-todo_time')
    return render(request, 'todo.html', {'todos': todos})

@csrf_exempt
def addTodo(request):
    format = '%b %d, %Y %I:%M %p'
    date = datetime.strptime((request.POST['date'] + ' ' + request.POST['time']), format)
    todo = TodoItem(
        todo_content=request.POST['content'],
        todo_time=date
    )
    todo.save()
    if (request.POST['browser'] == '1'):
        return HttpResponseRedirect('/todo/')
    else:
        return JsonResponse({'data':list(TodoItem.objects.values())})

@csrf_exempt
def delTodo(request):
    todo = TodoItem.objects.get(todo_id = request.POST['id'])
    todo.delete()
    if (request.POST['browser'] == '1'):
        return HttpResponseRedirect('/todo/')
    else:
        return JsonResponse({'data':list(TodoItem.objects.values())})

@csrf_exempt
def editTodo(request):
    todo = TodoItem.objects.get(todo_id = request.POST['id'])
    todo.todo_content = request.POST['content']
    todo.save()
    if (request.POST['browser'] == '1'):
        return HttpResponseRedirect('/todo/')
    else:
        return JsonResponse({'data':list(TodoItem.objects.values())})

@csrf_exempt
def viewTodo(request):
    data = list(TodoItem.objects.values())
    return JsonResponse({'data': data})

@csrf_exempt
def toggleTodo(request):
    todo = TodoItem.objects.get(todo_id = request.POST['id'])
    todo.todo_completed = not todo.todo_completed
    todo.save()
    if (request.POST['browser'] == '1'):
        return HttpResponseRedirect('/todo/')
    else:
        return JsonResponse({'data':list(TodoItem.objects.values())})