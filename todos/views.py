from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo


def todos_list_view(request):
    todos = Todo.objects.filter(author=request.user).order_by('-datetime_created')
    return render(request, 'todos/todos_list.html', {
        'todos': todos
    })
