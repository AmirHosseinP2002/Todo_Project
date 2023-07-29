from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Todo


def todos_list_view(request):
    todos = Todo.objects.filter(author=request.user).order_by('-datetime_created')
    return render(request, 'todos/todos_list.html', {
        'todos': todos
    })


def todo_detail_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todos/todo_detail.html', {
        'todo': todo,
    })
